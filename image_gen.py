import os
import openai
import requests

# https://platform.openai.com/docs/guides/images/usage
# https://platform.openai.com/docs/api-reference/images/create-edit


# Unique api_key for a user goes here and organization
openai.api_key = " "
openai.organization = " "
openai.Model.list()
# Folder name to store image
folder_name = ''
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)


def image_d(url, folder_name, num):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(response.content)


for i in range(50, 61):
    response = openai.Image.create(
        # Add prompt here
        prompt=" ",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_d(image_url, folder_name, i)

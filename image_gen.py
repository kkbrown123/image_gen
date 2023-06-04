import os
import openai
import requests

openai.api_key = "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"
openai.organization = "org-zAqoMaaF2XLgYGbUhS12hgJr"
openai.Model.list()

folder_name = 'kev_ima'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def image_d(url, folder_name, num):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(response.content)


for i in range(50,61):
    response = openai.Image.create(
    prompt=" logo for ceres robotics limited creates drone for  argiculture",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_d(image_url,folder_name,i)
    





import os
import requests

headers_={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def download_img(url, path, headers=headers_):
    if(os.path.exists(path)):
        print(f"file [{path}] existed")
        return

    response = requests.get(url,headers=headers)
    if response.status_code == 200 or response.status_code == 304:
        print(f"download : {url}")
        with open(path,'wb') as file:
            file.write(response.content)
            file.close()
    else:
        print(f'error : {response.status_code}  {url}')
import time
import requests
import os
import tools

def GetIllustList(word:str, page:int, page_max:int, mode:str ='all'):
    url = f'https://www.pixiv.net/ajax/search/illustrations/{word}?word={word}&order=date_d&mode={mode}&p={page}&csw=0&s_mode=s_tag_full&type=illust_and_ugoira&ai_type=1&lang=ja&version=26d18d57c15864f379c6224938a05ab88f587470'

    response = requests.get(url, headers=headers, cookies=cookies)

    condition = True

    if page_max >= 0:
        condition = page <= page_max
    else:
        condition = True

    if response.status_code == 200 and condition:
        result_json = response.json()
        if result_json.get('body') and result_json['body'].get('illust') and result_json['body']['illust']['data']:
            datas = result_json['body']['illust']['data']
            print(f"Get page {page} succeed. ")
            count = 0
            for d in datas:
                if d.get('id'):
                    count+=1
                    illust_url = f'https://www.pixiv.net/artworks/{d['id']}'
                    print(f'title : {d['title']}, url : {illust_url}')
                    # GetIllust(illust_url)
                    GetIllust(d.get('id'), word)
            print(f'page {page} illust count : {count}{'-' * 30}')

            GetIllustList(word, page + 1, page_max, mode)
        else:
            print('done')
    else:
        print('done')

def GetIllust(id, folder):
    url = f'https://www.pixiv.net/ajax/illust/{id}/pages?lang=jp&version=36708994901981268c36d47831f566a7ceb62f39'
    response = requests.get(url, headers=headers, cookies=cookies)
    body = response.json()['body']
    if body:
        for b in body:
            u = b['urls']['original']
            # print(f'   {u}')
            tools.download_img(u, f'{folder}/{u.split('/')[-1]}',headers)
            time.sleep(1)

    pass

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://www.pixiv.net/'
}

cookies = {
    'PHPSESSID': '6262491_CXwNHqpYvUVbyqXaiLxuCZtm0sM6QU8b'
}

# word = '%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A9%E3%82%A6' #アルフォウ
# word = '%E3%83%80%E3%82%A4%E3%83%89%E3%83%BC'
mode = 'all' #all, safe, r18

def test():
    if not os.path.exists(rf'{'アルフォウ'}'):
        os.mkdir(rf'{'アルフォウ'}')

    GetIllustList('アルフォウ', 1, 2)
    pass

def main():
    word = input('輸入關鍵字:')

    page = int(input('輸入開始頁數:'))
    page_max = int(input('輸入最大頁數:'))
    print(f'開始搜尋 : {word}, 起始頁數 : {page}, 最大頁數 : {page_max}')

    if not os.path.exists(rf'{word}'):
        os.mkdir(rf'{word}')

    GetIllustList(word, page, page_max)
    pass

if __name__ == '__main__':
    main()
    # test()
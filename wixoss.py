import requests
from bs4 import BeautifulSoup
import json
import os
import tools
import pandas

def GetCardList(page):
    # url = f'https://www.takaratomy.co.jp/products/wixoss/card/card_list.php?card_page={page}&keyword=&card_kind=&card_type=&rarelity=&support_formats=2&story=&level=&color=&ability=&keyword_target=%E3%82%AB%E3%83%BC%E3%83%89No,%E3%82%AB%E3%83%BC%E3%83%89%E5%90%8D,%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97,%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88,%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC,%E3%83%95%E3%83%AC%E3%83%BC%E3%83%90%E3%83%BC&product_type=&product_id=&product_no=&newadd=&pageflg=1'
    # url = f'https://www.takaratomy.co.jp/products/wixoss/card/card_list.php?card_page={page}&keyword=&card_kind=&card_type=&rarelity=&support_formats=2&story=&&level=&color=&ability=6&keyword_target=%E3%82%AB%E3%83%BC%E3%83%89No,%E3%82%AB%E3%83%BC%E3%83%89%E5%90%8D,%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97,%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88,%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC,%E3%83%95%E3%83%AC%E3%83%BC%E3%83%90%E3%83%BC&product_type=&product_id=&product_no=&newadd='
    # url = f'https://www.takaratomy.co.jp/products/wixoss/card/card_list.php?card_page={page}&keyword=&card_kind=&card_type=&rarelity=&support_formats=2&story=&&level=&color=&ability=3,5&keyword_target=%E3%82%AB%E3%83%BC%E3%83%89No,%E3%82%AB%E3%83%BC%E3%83%89%E5%90%8D,%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97,%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88,%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC,%E3%83%95%E3%83%AC%E3%83%BC%E3%83%90%E3%83%BC&product_type=&product_id=&product_no=&newadd='
    # url = f'https://www.takaratomy.co.jp/products/wixoss/card/card_list.php?card_page={page}&keyword=&card_kind=&card_type=&rarelity=&support_formats=2&story=&&level=&color=&ability=17,21&keyword_target=%E3%82%AB%E3%83%BC%E3%83%89No,%E3%82%AB%E3%83%BC%E3%83%89%E5%90%8D,%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97,%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88,%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC,%E3%83%95%E3%83%AC%E3%83%BC%E3%83%90%E3%83%BC&product_type=&product_id=&product_no=&newadd='
    # url = f'https://www.takaratomy.co.jp/products/wixoss/card/card_list.php?card_page={page}&keyword=&card_kind=&card_type=&rarelity=&support_formats=2&story=&&level=&color=&ability=11,12,13,14,15,16&keyword_target=%E3%82%AB%E3%83%BC%E3%83%89No,%E3%82%AB%E3%83%BC%E3%83%89%E5%90%8D,%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97,%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88,%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC,%E3%83%95%E3%83%AC%E3%83%BC%E3%83%90%E3%83%BC&product_type=&product_id=&product_no=&newadd='
    url = f'https://www.takaratomy.co.jp/products/wixoss/card/card_list.php?card_page={page}&product_no=WXi-16&keyword=&card_kind=&card_type=&rarelity=&support_formats=2&story=&&level=&color=&ability=&keyword_target=%E3%82%AB%E3%83%BC%E3%83%89No,%E3%82%AB%E3%83%BC%E3%83%89%E5%90%8D,%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97,%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88,%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC,%E3%83%95%E3%83%AC%E3%83%BC%E3%83%90%E3%83%BC&product_type=booster&product_id=&product_no=WXi-16&newadd='
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        cardsUrl = soup.find_all('a', class_="c-box")
        if cardsUrl:
            print(f"Get page {page} succeed")
            for u in cardsUrl:
                cardList.append(GetCardData(u['href']))

            GetCardList(page+1)
        else:
            with open(rf"test_output/wixoss_card_list.txt", 'w', encoding='utf-8') as file:
                # file.write("\n".join(str(item) for item in cardList))
                json.dump(cardList, file, ensure_ascii=False, indent=4)

            cardList_excel = []
            for card in cardList:
                card_handled = []
                card_handled.append(card['cardNum'])
                card_handled.append(card['cardPack'])
                card_handled.append(card['cardName'])
                card_handled.append(card['cardRarity'])
                card_handled.append(card['cardImg'])
                for d in card['detail'].values():
                    card_handled.append(d)

                cardList_excel.append(card_handled)

            data = pandas.DataFrame(cardList_excel)
            data.to_excel("test_output/p16cardlist.xlsx",sheet_name='sheet1',index=False)

            print('done')
    else:
        with open(rf"test_output/wixoss_card_list.txt", 'w', encoding='utf-8') as file:
            # file.write("\n".join(str(item) for item in cardList))
            json.dump(cardList, file, ensure_ascii=False, indent=4)
        print(f'Get page {page} failed')

def GetCardData(url):
    cardDetail = {}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        cardNo = soup.find("p", class_="cardNum").text
        cardNoSplit = cardNo.split("-")
        cardDetail["cardNum"] = cardNo
        cardPack = cardNoSplit[1] if cardNoSplit.__len__() == 3 else cardNoSplit[0]
        cardDetail['cardPack'] = cardPack
        cardDetail["cardName"] = soup.find("p", class_="cardName").text.replace("\u3000", " ")
        cardDetail["cardRarity"] = soup.find("div",class_="cardRarity").text
        cardImg = soup.find("div",class_="cardImg").img["src"]
        cardDetail["cardImg"] = cardImg

        if not os.path.exists(rf'test_output/{cardPack}'):
            os.mkdir(rf'test_output/{cardPack}')

        tools.download_img(cardImg, rf'test_output/{cardPack}/{cardNo}.jpg')

        cardData = soup.find("div", class_="cardData")
        cardDetail["detail"] = HandleCardDetail(cardData.find_all("dt"), cardData.find_all("dd"))
        cardSkill = cardData.find_all("div", class_="cardSkill")
        if cardSkill:
            cs_list = []
            for cs in cardSkill:
                cs_list.append(ReplaceCardSkillContent(cs.contents))
            cardDetail["cardSkill"] = cs_list
        cardText = cardData.find("div", class_="cardText")
        if cardText:
            cardDetail["cardText"] = cardText.text.replace("\n","").strip().replace("\u3000", " ")
        cardFaq = cardData.find("div", class_="cardFaq")
        if cardFaq:
            cardDetail["cardFaq"] = HandleCardFaq(cardFaq)

        # print(cardDetail)
        print(f'get {cardNo} {cardDetail["cardName"]}\'s data done')
    else:
        print(f"Get card {url} failed")

    return cardDetail

def HandleCardDetail(key, value):
    detail = {}
    for i in range(0, 12):
        key_m = key[i].text.replace("\n", "").strip()
        value_m = ""
        if key_m == "フォーマット":
            value_m = "".join(str(item) for item in value[i].contents).replace("\n", "").strip()
            value_m = value_m.replace("<img alt=\"《キーアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_format_key.png\">", "《キー》")
            value_m = value_m.replace("<img alt=\"《ディーヴァアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_format_diva.png\"/></img>", "《ディーヴァ》")
        else:
            value_m = value[i].text.replace("\n", "").strip()

        detail[key_m] = value_m
    return detail

def HandleCardFaq(data):
    faq = []
    _q = data.find_all("dt")
    _a = data.find_all("dd")

    for i in range(0, _q.__len__()):
        q = _q[i].text
        q = q.replace("\n", "").strip().replace("\u3000", " ")
        a = _a[i].text
        a = a.replace("\n", "").strip().replace("\u3000", " ")
        faq.append({q: a})

    return faq

def ReplaceCardSkillContent(page_element_list):
    result = str("").join(str(item) for item in page_element_list)
    result = result.replace("<img alt=\"【出】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_arrival.png\"/>", "【出】")
    result = result.replace("<img alt=\"【常】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_regular.png\"/>", "【常】")
    result = result.replace("<img alt=\"【自】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_auto.png\"/>", "【自】")
    result = result.replace("<img alt=\"【起】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_starting.png\"/>", "【起】")

    result = result.replace("<img alt=\"【チーム】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_team.png\"/>", "【チーム】")
    result = result.replace("<img alt=\"【ドリームチーム】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_dreamteam.png\"/>", "【ドリームチーム】")
    result = result.replace("<img alt=\"【チーム出】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_arrival_team.png\"/>", "【チーム出】")
    result = result.replace("<img alt=\"【チーム常】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_regular_team.png\"/>", "【チーム常】")
    result = result.replace("<img alt=\"【チーム自】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_auto_team.png\"/>", "【チーム自】")
    result = result.replace("<img alt=\"【チーム起】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_starting_team.png\"/>", "【チーム起】")
    result = result.replace("<img alt=\"【使用条件】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_terms_use.png\"/>", "【使用条件】")

    result = result.replace("<img alt=\"《コインアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_coin.png\"/>", "○")

    result = result.replace("<img alt=\"《無》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_null.png\"/>", "《無》")
    result = result.replace("<img alt=\"《赤》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_red.png\"/>", "《赤》")
    result = result.replace("<img alt=\"《青》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_blue.png\"/>", "《青》")
    result = result.replace("<img alt=\"《緑》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_green.png\"/>", "《緑》")
    result = result.replace("<img alt=\"《黒》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_black.png\"/>", "《黒》")
    result = result.replace("<img alt=\"《白》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_white.png\"/>", "《白》")
    result = result.replace("<img alt=\"《無×0》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_null_00.png\"/>", "《無×0》")
    result = result.replace("<img alt=\"《赤×0》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_red_00.png\"/>", "《赤×0》")
    result = result.replace("<img alt=\"《青×0》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_blue_00.png\"/>", "《青×0》")
    result = result.replace("<img alt=\"《緑×0》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_green_00.png\"/>", "《緑×0》")
    result = result.replace("<img alt=\"《黒×0》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_black_00.png\"/>", "《黒×0》")
    result = result.replace("<img alt=\"《白×0》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_white_00.png\"/>", "《白×0》")
    result = result.replace("<img alt=\"《無×1》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_null_01.png\"/>", "《無×1》")
    result = result.replace("<img alt=\"《赤×1》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_red_01.png\"/>", "《赤×1》")
    result = result.replace("<img alt=\"《青×1》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_blue_01.png\"/>", "《青×1》")
    result = result.replace("<img alt=\"《緑×1》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_green_01.png\"/>", "《緑×1》")
    result = result.replace("<img alt=\"《黒×1》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_black_01.png\"/>", "《黒×1》")
    result = result.replace("<img alt=\"《白×1》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_white_01.png\"/>", "《白×1》")

    result = result.replace("<img alt=\"《ダウン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_down.png\"/>", "《ダウン》")
    result = result.replace("<img alt=\"《ターン１回》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_turn_01.png\"/>", "《ターン１回》")
    result = result.replace("<img alt=\"《ターン２回》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_turn_02.png\"/>", "《ターン２回》")
    result = result.replace("<img alt=\"《ゲーム１回》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_game_01.png\"/>", "《ゲーム１回》")
    result = result.replace("<img alt=\"《メインフェイズアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_phase_main.png\"/>", "《メインフェイズアイコン》")
    result = result.replace("<img alt=\"《アタックフェイズアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_phase_attack.png\"/>", "《アタックフェイズ》")
    result = result.replace("<img alt=\"《ディソナアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_dissona.png\"/>", "《ディソナ》")
    result = result.replace("<img alt=\"《ガードアイコン》\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_guard_mini.png\"/>", "《ガードアイコン》")
    result = result.replace("<img alt=\"【ライズ】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_rise_01.png\"/>", "【ライズ】")
    result = result.replace("<img alt=\"【ハーモニー】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_harmony.png\"/>", "【ハーモニー】")
    result = result.replace("<img alt=\"【　　】\" height=\"23\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_frame_null.png\"/>", "【　　】")
    result = result.replace("<img alt=\"ライフバースト\" height=\"24\" src=\"https://www.takaratomy.co.jp/products/wixoss/img/card/icon/icon_txt_burst.png\" width=\"26\"/>", "【ライフバースト】")

    result = result.replace("<br>", "")
    result = result.replace("</br>", "")
    result = result.replace("<br/>", "")
    # result = result.replace("\n", "")
    result = result.strip()
    result = result.replace("\u3000", " ")
    return result

def HandleStr(self: str):
    result = self.replace("\n", "")
    result = result.strip()
    result = result.replace("\u3000", " ")
    return result

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

cardList = []

GetCardList(1)

os.system('pause')


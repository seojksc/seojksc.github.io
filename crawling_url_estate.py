import requests
import json
import logging
import datetime

import os

from bs4 import BeautifulSoup


if __name__ == "__main__" :
 print("\n")
 print("#=====================================================")
 cur_time = datetime.datetime.now()
 print("검색날짜(현재시각) : %s" % cur_time)
 print("#=====================================================\n")



URL = "https://m.land.naver.com/complex/getComplexArticleList"

param = {
    'hscpNo': '16949',
    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

############################################
res = requests.get(URL)
#res = requests.get(URL, params=param, headers=header)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())
#print(title)
print('화순삼천한양립스')
## HTML 문을 보기좋게 정렬하기
#print(soup.prettify())
############################################



logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

#################################################################################

param = {
    'hscpNo': '16949',
#    'tradTpCd': 'A1',
    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break


#################################################################################

param = {
    'hscpNo': '16949',
#    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

print('#=========================================\n')
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################



URL = "https://m.land.naver.com/complex/getComplexArticleList"

param = {
    'hscpNo': '106429',
    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

############################################
res = requests.get(URL)
#res = requests.get(URL, params=param, headers=header)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())
#print(title)
print('화순 한국아델리움')
## HTML 문을 보기좋게 정렬하기
#print(soup.prettify())
############################################



logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

#################################################################################

param = {
    'hscpNo': '106429',
#    'tradTpCd': 'A1',
    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break


#################################################################################

param = {
    'hscpNo': '106429',
#    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

print('#=========================================\n')
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################



URL = "https://m.land.naver.com/complex/getComplexArticleList"

param = {
    'hscpNo': '105083',
    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

############################################
res = requests.get(URL)
#res = requests.get(URL, params=param, headers=header)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())
#print(title)
print('화순 대성베르힐')
## HTML 문을 보기좋게 정렬하기
#print(soup.prettify())
############################################



logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

#################################################################################

param = {
    'hscpNo': '105083',
#    'tradTpCd': 'A1',
    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break


#################################################################################

param = {
    'hscpNo': '105083',
#    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break


print('#=========================================\n')
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################



URL = "https://m.land.naver.com/complex/getComplexArticleList"

param = {
    'hscpNo': '16946',
    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

############################################
res = requests.get(URL)
#res = requests.get(URL, params=param, headers=header)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())
#print(title)
print('화순 대광로제비앙')
## HTML 문을 보기좋게 정렬하기
#print(soup.prettify())
############################################



logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

#################################################################################

param = {
    'hscpNo': '16946',
#    'tradTpCd': 'A1',
    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break


#################################################################################

param = {
    'hscpNo': '16946',
#    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

print('#=========================================\n')
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################




URL = "https://m.land.naver.com/complex/getComplexArticleList"

param = {
    'hscpNo': '125042',
    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

############################################
res = requests.get(URL)
#res = requests.get(URL, params=param, headers=header)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())
#print(title)
print('화순 삼일파라뷰에듀시티')
## HTML 문을 보기좋게 정렬하기
#print(soup.prettify())
############################################



logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

#################################################################################

param = {
    'hscpNo': '125042',
#    'tradTpCd': 'A1',
    'tradTpCd': 'B1',
#    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break


#################################################################################

param = {
    'hscpNo': '125042',
#    'tradTpCd': 'A1',
#    'tradTpCd': 'B1',
    'tradTpCd': 'B2',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
#        if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#        if float(item['spc2']) < 40 or float(item['spc2']) > 50:
        if float(item['spc2']) < 20 or float(item['spc2']) > 200:   # 집 면적
            continue
        logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break

print('#=========================================\n')
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################

os.system("pause")

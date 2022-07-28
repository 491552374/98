# -*- coding = utf-8 -*-
# @Time : 2021/6/8 0025 11:20
# @Author : 铭仔
# @File : 98.py
# @Software : PyCharm

from urllib import request
import os
import time
from tqdm import tqdm
import signal
import sys
import threading
import socket
import request

socket.setdefaulttimeout(5)

requestURL = 'https://www.981awsad.xyz/'


def get_info(site, titles, links):
    resp = request.session_get(site)
    a_list = resp.xpath('//table[@id="threadlisttableid"]//tbody[starts-with(@id, "normalthread_")]//a[@class="s xst"]')
    for a in a_list:
        titles.append(a.xpath('./text()')[0])
        links.append(requestURL + a.xpath('./@href')[0])


def download_img(title, link):
    nomakechar = [":", "/", "\\", "?", "*", "“", "<", ">", "|", "”"]
    for item in nomakechar:
        if title.find(item) > -1:
            title = title.replace(item, '')
    if not os.path.exists('G'):
        os.makedirs('G')

    resp = request.session_get(link)
    img_list = resp.xpath('//img[@class="zoom"]')
    magnet_list = resp.xpath('//div[@class="blockcode"]//li/text()')
    magnet = open('G/' + title + '.txt', "w+")
    for m in magnet_list:
        magnet.write(m + '\n')
    magnet.close()
    pbar = tqdm(total=len(img_list))
    for i in img_list:
        file_name = 'G/' + title + '(' + str(img_list.index(i)) + ').jpg'
        download_link = i.xpath('./@file')
        if len(download_link) > 0:
            if not os.path.exists(file_name):
                index = 1
                while index <= 1:
                    try:
                        re = request.get_file(download_link[0])
                        with open(file_name, 'wb') as f:
                            f.write(re.content)
                    except:
                        index += 1
                        continue
                    else:
                        break

        pbar.update(1)
    pbar.close()


def quit():
    print("Bye!")
    sys.exit(0)


def work():
    url_type = input("请输入下载的类型[国产原创:2,亚洲无码原创:36,亚洲有码原创:37,欧美无码:38,高清中文字幕:103,韩国主播:152] =>>>> :")
    resp = request.session_get(requestURL + 'forum-' + url_type + '-1.html')
    pages_xml = resp.xpath('//span[@id="fd_page_top"]//label/span/@title')
    pages = pages_xml[0].replace("共", "").replace("页", "").replace(" ", "")
    print("共 %s 页" % pages)
    sPage = input("请输入开始下载的页数：")
    page = int(sPage)
    ePage = input("请输入结束下载的页数：")
    while page < int(ePage) and page < int(pages):
        # while int(page) < 1:
        site = requestURL + 'forum-' + url_type + '-' + str(page) + ".html"
        titles = []
        links = []
        get_info(site, titles, links)

        for i in range(0, len(titles)):
            print('#' * 100)
            print('第' + str(page) + '页数据,共' + str(len(titles)) + '条帖子 =>>>> 正在下载第' + str(i + 1) + '个帖子 =>>>> ' + titles[i])
            download_img(titles[i], links[i])
            print('#' * 100 + '\n\n')
            time.sleep(1)
        page += 1
    quit()


def main():
    work_thread = threading.Thread(target=work)
    work_thread.daemon = True
    work_thread.start()
    signal.signal(signal.SIGINT, quit)
    print("Start Working")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()

# -*- coding = utf-8 -*-
# @Time : 2021/5/25 0025 11:20
# @Author : 铭仔
# @File : request.py
# @Software : PyCharm

import requests
import time
from lxml import etree
import traceback


# 请求网站信息
def req(url, referer, sleep):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'referer': referer,
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    }
    try:
        time.sleep(sleep)
        response = requests.get(url, headers=headers)  # 加请求头,如果需要加随机请求头和代理ip
        resp = etree.HTML(response.text)
        return resp
    except Exception as e:
        traceback.print_exc()


def get(url, sleep):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }
    try:
        time.sleep(sleep)
        response = requests.get(url, headers=headers)  # 加请求头,如果需要加随机请求头和代理ip
        resp = etree.HTML(response.text)
        return resp
    except Exception as e:
        traceback.print_exc()


def session(url, sleep):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    try:
        time.sleep(sleep)
        session = requests.session()
        session.headers.update(headers)
        response = session.get(url)  # 加请求头,如果需要加随机请求头和代理ip
        resp = etree.HTML(response.text)
        return resp
    except Exception as e:
        traceback.print_exc()


def session_coding(url, sleep, coding):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    }
    try:
        time.sleep(sleep)
        session = requests.session()
        session.headers.update(headers)
        response = session.get(url)  # 加请求头,如果需要加随机请求头和代理ip
        response.encoding = coding
        resp = etree.HTML(response.text)
        return resp
    except Exception as e:
        traceback.print_exc()


def session_get(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    try:
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        session = requests.session()
        session.keep_alive = False
        session.headers.update(headers)
        response = session.get(url)  # 加请求头,如果需要加随机请求头和代理ip
        resp = etree.HTML(response.text)
        return resp
    except Exception as e:
        traceback.print_exc()


def get_file(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    try:
        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
        session = requests.session()
        session.keep_alive = False
        session.headers.update(headers)
        response = session.get(url)  # 加请求头,如果需要加随机请求头和代理ip
        return response
    except Exception as e:
        traceback.print_exc()

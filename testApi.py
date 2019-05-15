#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
自动化接口测试 by charlie liu
'''
import unittest
import json
import requests
class Logout(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

class Run(Logout):
 # 科室判断节口
    def test_keshi_api(self):
        param = {"s": "白癜风怎么治疗", "a": 2}
        url = 'http://domain.com/api/auto'
        r = requests.get(url, params=param)
        r = r.json()
        self.assertEqual(r["status"], 200)

 # 关键词相关接口
    def test_relate(self):
        param = {"word": "白癜风"}
        url = 'https://domain.com/api/GetListByWord'
        r = requests.get(url, params=param)
        r = r.json()
        self.assertIsNotNone(r)
 # 最新新闻接口
    def test_news(self):
        url = 'https://domain.com/api/news'
        r = requests.get(url)
        r = r.json()
        self.assertIsNotNone(r)
 # 最新新闻接口
    def test_yao_news(self):
        url = 'https://domain.com/api/YaoNews'
        r = requests.get(url)
        r = r.json()
        self.assertIsNotNone(r)
if __name__ == '__main__':
    unittest.main()

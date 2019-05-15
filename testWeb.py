#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
自动化接口测试 by charlie liu
'''

from selenium import webdriver
#from selenium.webself.support.ui import WebDriverWait
import unittest
import time

class Logout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            r"C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.6\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.get("http://news.120ask.com")
        print('start')
    def tearDown(self):
        print('end')
class WebTest(Logout):
    #是否能打开网站，打开时间
    def test_index(self):
            assert len(self.driver.find_elements_by_css_selector('.mid-cont .part')), "判断数据存在条数："
            count = len(self.driver.find_elements_by_css_selector('.mid-cont .part'))
            self.assertEqual(count, 30)
    #是否有左侧分类，大分类数量
    def test_fenlei(self):
        self.test_index()
        assert len(self.driver.find_elements_by_css_selector('.left-nav .part')), "判断分类条数："
        category_counts = len(self.driver.find_elements_by_css_selector('.left-nav .part'))
        self.assertEqual(6 ,category_counts)
        #可以判断下分类数量什么的省略了
    #首页列表数量（第一页）
    def test_index_list(self):
        assert len(self.driver.find_elements_by_css_selector('.mid-cont .part')), "判断文章列表条数："
        list_counts = len(self.driver.find_elements_by_css_selector('.mid-cont .part'))
        self.assertEqual(30,list_counts)
    #焦点图数量或存在与否
    def test_index_focus(self):
        assert len(self.driver.find_elements_by_css_selector('.slider .images li')), "判断焦点图条数："
        list_counts = len(self.driver.find_elements_by_css_selector('.slider .images li'))
        self.assertEqual(6 , list_counts)
        print(list_counts)
        # 可以判断下焦点图是否存在省略了
    #热点数量
    def test_index_hot(self):
        i = 0
        assert len(self.driver.find_elements_by_css_selector('.hot-article ul li')), "判断热点图条数："
        focus_counts = len(self.driver.find_elements_by_css_selector('.hot-article ul li'))
        self.assertEqual(5 , focus_counts)
        print(focus_counts)
    #查看SEO信息是否完整
    def test_index_seo(self):
            assert self.driver.title,'标题是否存在：'
            self.assertIsNotNone(self.driver.title)
            assert self.driver.find_element_by_xpath("//meta[@name='keywords']"),'关键词是否存在：'

            self.assertIsNotNone(self.driver.find_element_by_xpath("//meta[@name='keywords']"))

            assert self.driver.find_element_by_xpath("//meta[@name='description']"), '描述是否存在：'

            self.assertIsNotNone(self.driver.find_element_by_xpath("//meta[@name='description']"))
    #测试表单递交
    def test_index_submit(self):
        assert self.driver.find_element_by_xpath("//input[@name='kw']"), '搜索是否存在：'
        self.assertIsNotNone(self.driver.find_element_by_xpath("//input[@name='kw']"))
        elem = self.driver.find_element_by_xpath("//input[@name='kw']")
        elem.send_keys(r"轻度地贫")
        # 提交表单
        self.driver.find_element_by_xpath("//*[@class='button']").click(),'点击是否成功：'
        assert self.driver.title.encode("utf-8") ,"递交是否成功"
        title = self.driver.title.encode("utf-8")
        self.assertIn("搜索",title)
        time.sleep(5)

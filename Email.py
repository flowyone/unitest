#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
自动化接口测试 by charlie liu
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Mail:
    def send_mail(self,message):
        sender = '420619280@qq.com'
        pwd  = '密码'#密码要保密了，谢谢
        receivers = ['441747382@qq.com']  # 接收邮件
        #  utf-8 设置编码
        message = MIMEText(message, 'plain', 'utf-8')
        message['From'] = Header("写信不成功打死你", 'utf-8')  # 发送者
        message['To'] = Header("接受不成功砍死你", 'utf-8')  # 接收者

        subject = 'Python 自动化测试邮件'
        message['Subject'] = Header(subject, 'utf-8')
        #try 一下看BUG
        try:
            smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 456)# 邮件服务器及端口号
            smtpObj.login(sender, pwd)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import requests
import time
import threading
import sys

username='用户名' #用户名和密码需要更改
password='你的密码'
timeWaite=60 #可以设定每个30秒检查网络

def Connect():
	# 构造请求数据
	url='http://222.204.3.221:801/include/auth_action.php'
	payload = {
		'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
		'Connection':'keep-alive',
		'action':'login',
		'username':username,
		'password':password,
		'ac_id':1,
		'save_me':1,
		'ajax':1,
		'user_ip': '',
		'nas_ip': '',
		'user_mac': ''
	}
	# 调用requests
	r=requests.post(url,data=payload)
	# 显示是否连接
	for i in range(1,7):
		time.sleep(0.2)
		print('.')
	if r.status_code == 200:
		print('NCUWLAN 连接成功！')
	else:
		print('NCUWLAN 被吃掉了么，连不上诶')

def isConnected():
	# 调用requests连接百度查看是否连接，返回 true 或者False
	try:
		baidu=requests.get('https://www.baidu.com/',timeout=7)
		if baidu.status_code == requests.codes.ok:
			print('路面畅通，随时可以开车！')
			return True
		else:
			print('好像无法连接到网络：)')
			return False
	except Exception as e:
		print('好像无法连接到网络:)')
		return False

def printHe():
	a='请稍等片刻'
	flower=[a+'/',a+'-',a+'\\',a+'|']
	i=0
	while True:
		print(flower[i%4]+'\r',end='')
		# sys.stdout.write(flower[i%4]+'\r')
		# 原本我用stdout的write方法，但是不兼容23，用print其实也可以的
		# 后面加\r会让输入光表调到行首
		sys.stdout.flush()
		# flush会让之前的打印变成水上的浮萍，可以抹掉
		time.sleep(0.5)
		i=i+1

t1=threading.Thread(target=printHe)
# 设置线程t1
t1.setDaemon(True)
t1.start()
# 设置线程t1为守护模式
# 运行t1，t1将会伴随主线程一直跑

while True:
	nCode = isConnected()
	if nCode :
		print('NCUWLAN 畅通')
		print(timeWaite+'s后我会帮您再检测网络\n\n')
	else:
		print('NCUWLAN, 正在尝试重新连接:)')
		Connect()
		print(timeWaite+'s后我会帮您再检测网络\n\n')
	time.sleep(timeWaite)
#test

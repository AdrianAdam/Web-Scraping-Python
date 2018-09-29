import socket
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
import re
import time

Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1'
Port = 8080

Sock.bind((Host,Port))

Sock.listen(1)

client, addresse = Sock.accept()

while 1:
	RequeteDuClient = client.recv(255)
	if not RequeteDuClient:
		break

	myString = ""

	for i in range(0,len(RequeteDuClient)):
		myString += chr(RequeteDuClient[i])

	myString2 = myString.split(",")

	driver = webdriver.Chrome('/usr/bin/chromedriver')
	driver.get("https://www.emag.ro/homepage")
	search = driver.find_element_by_class_name("searchbox-main")
	search.send_keys(myString2[0])
	search.send_keys(Keys.RETURN)
	submit = driver.find_element_by_class_name("searchbox-submit-button")
	submit.click()

	data = driver.current_url
	r = requests.get(data)
	data = r.text
	soup = BeautifulSoup(data, "lxml")

	if len(myString2) >= 1:
		for i in range(1, len(myString2)):
			driver.find_element_by_partial_link_text(myString2[i]).click()

	time.sleep(5)
	data = driver.current_url
	r = requests.get(data)
	data = r.text
	soup = BeautifulSoup(data, "lxml")

	for s in soup.findAll('sup'):
		s.extract()

	tags = soup.findAll("div", class_="card-item js-product-data")
	prices = soup.findAll("p", class_="product-new-price")
	
	for i in range(0, len(tags)):
		print(tags[i].attrs['data-name'])
		print(prices[i].text)
		print("\n")
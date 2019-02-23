import requests
from pprint import pprint 
from bs4 import BeautifulSoup
# from tabulate import tabulate
def top50():
	url = requests.get("https://www.timeshighereducation.com/student/best-universities/top-50-universities-reputation-2018#survey-answer")
	soup = BeautifulSoup(url.text,"html.parser")
	table = soup.find("table", width = "746")
	tbody = soup.find("tbody")
	tr = tbody.find_all("tr")
	top_50 = []
	for i in tr[1:]:
		University_details = {}
		a = i.getText().strip().split("\n")
		url = i.find("a").get("href")
		University_details["World Reputation Rank 2018"] = a[0]
		University_details["World Reputation Rank 2017"] = a[1]
		University_details["University name"] = a[2]
		University_details["Country/Region"] = a[3]
		University_details["World University Rank 2018"] = a[4]
		University_details["url"] = url
		# pprint (University_details)
		top_50.append(University_details.copy())
	return top_50
University_details = top50()
# pprint University_datails


def more_about():
	more_details = []
	for i in University_details:
		more_about_university = {}
		url = i["url"]
		url1 = requests.get(url)
		soup = BeautifulSoup(url1.text,"html.parser")
		div = soup.find("div", class_  = "region region-content")
		divs = div.find("div", class_= "institution-info__contact-detail").getText().strip()
		more_about_university["Address"] = divs
		class1 = soup.find("ul", class_ = "courses-list-group list-group")
		# print (class1)
		
		# print (more_about_university)


		all_cources = []
		courses = class1.find_all("ul")
		for l in courses:
			courses_name = l.getText().strip().split("\n")
			all_cources.append(courses_name)
		# print (all_cources)
		name = class1.find_all("h3")
		count = 0
		for j in name:
			more_about_university[j.getText()] = all_cources[count]
			count += 1
		print (more_about_university)
		break 

more_about()
	
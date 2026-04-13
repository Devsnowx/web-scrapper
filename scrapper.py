#! /usr/bin/python3

#web word-password-scrapper python script

#import modules needed


import re
import requests
from bs4 import BeautifulSoup

print('''                         
                                                   
                                                   
 ░███████  ░████████   ░███████  ░██    ░██    ░██ 
░██        ░██    ░██ ░██    ░██ ░██    ░██    ░██ 
 ░███████  ░██    ░██ ░██    ░██  ░██  ░████  ░██  
       ░██ ░██    ░██ ░██    ░██   ░██░██ ░██░██   
 ░███████  ░██    ░██  ░███████     ░███   ░███    
  APR-13-2026                                               
                                                   
                                                                                   
        	 *************************
        	 *   WEB WORD SCRAPER    *
        	 *************************
                 WELCOME TO SNOWWORLD.....
                 ENJOY USING THIS TOOL....
                          
''')
#prompt user to enter (url,min_length,max_length,outputfile):
url = input('Enter Target url: ')
min_length=int(input('Enter min character length: '))
max_length=int(input('Enter min character length: '))
outputfile=input('Enter preffered output file name(eg.word.txt): ')

#grab content from the web
try :
	response=requests.get(url)
	if response.status_code != 200:
		print('⛔️URL FETCHING ERROR!')
		exit
except requests.exceptions.RequestException:
    print("⛔️ URL FETCHING ERROR!")
    exit()
#parse the data using beautifulsoup bs4
#set variable e.g 
soup=BeautifulSoup(response.content, 'html.parser')

#gather all the text from the website

text=soup.get_text()

#use regex(regular expression[{import re} module]) 

words=re.findall(r'\b\w+\b', text)

#fiter the words based on user input
filteredwords=[word for word in words if min_length <=len(word)<=max_length]

#the filtered words to be saved

with open(outputfile, 'w') as file:
	for word in filteredwords:
		file.write(word + '\n')
  

from bs4 import BeautifulSoup
import requests
import re
import urllib
def getURLData(url):
    response = requests.get(url)
    return response.text
user_input = input("Enter the url you want to search!\n")
document = getURLData(user_input)
read_doc = BeautifulSoup(document, 'html.parser')
print("Social links are:")
for link in read_doc.find_all('a',
                          attrs={'href': re.compile("^https://")}):
    print(link.get('href'))
Email = urllib.request.urlopen(user_input)
print("Email id are:")
for mails in Email:
    s =mails.decode().strip()
    exp_for_email = re.findall(r"[A-Za-z0-9._%+-]+"
                     r"@[A-Za-z0-9.-]+"
                     r"\.[A-Za-z]{2,4}",s)
    print(exp_for_email)
print("Telephone number are:")
Telephone=urllib.request.urlopen(user_input)
for number in Telephone:
    exp_for_tele=re.findall("^\+?[0-9]{0,1}?[-\s]?\(?[0-9]{3}?\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$", s)
    print(exp_for_tele)
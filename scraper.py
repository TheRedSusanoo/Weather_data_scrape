import requests
import bs4
import datetime
import lxml
import html
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def extract_city_result(soupy, city_name):
    city_result = [city_name]
    x = soupy.select('span')
    city_result.append(str(x[4].text))
    for i in range(6, 8):
        city_result.append(str(x[i].text))
    city_result.append(str(x[5].text))

    print(city_result)
    return city_result





now = datetime.datetime.now()
date = str(now.day) + "/%d/"%now.month + str(now.year)
time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
timestamp = [date, time]
str_con = ""

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Scraper-18f218884efc.json', scope)
xp = gspread.authorize(credentials)
worksheet = xp.open('Weather report').sheet1

temps = []
New_York = requests.get("https://www.google.com/search?q=new+york+weather")
New_York_soup = bs4.BeautifulSoup(New_York.content, 'lxml')


Tokyo = requests.get("https://www.google.com/search?q=tokyo+weather")
Tokyo_soup = bs4.BeautifulSoup(Tokyo.content, 'lxml')

Delhi = requests.get("https://www.google.com/search?q=delhi+weather")
Delhi_soup = bs4.BeautifulSoup(Delhi.content, 'lxml')

Guadalajara = requests.get("https://www.google.com/search?q=guadalajara+weather")
Guadalajara_soup = bs4.BeautifulSoup(Guadalajara.content, 'lxml')

London = requests.get("https://www.google.com/search?q=london+weather")
London_soup = bs4.BeautifulSoup(London.content, 'lxml')

soups = [[New_York_soup, 'New York'], [Tokyo_soup, 'Tokyo'], [Delhi_soup, 'Delhi'], [Guadalajara_soup, 'Guadalajara'], [London_soup, 'London']]

worksheet.append_row(timestamp)
worksheet.append_row(['City', 'Current Temperature', 'Max', 'Min', 'Wind Speed'])

for it in range(len(soups)):
    worksheet.append_row(extract_city_result(soups[it][0], soups[it][1]))

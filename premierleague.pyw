from bs4 import BeautifulSoup
import requests
from datetime import datetime
from datetime import timedelta
from win11toast import toast
team_name = 'chelsea'
url = f"https://www.skysports.com/{team_name}-fixtures"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
date = soup.find('h4', class_='fixres__header2').text
comp = soup.find('h5', class_='fixres__header3').text
tag = soup.find('span', class_ ='matches__item-col matches__participant matches__participant--side2')
if tag.find('span', class_='swap-text__target').text.title() == team_name.title():
    tag = soup.find('span', class_ ='matches__item-col matches__participant matches__participant--side1')
team = tag.find('span', class_='swap-text__target').text
time = soup.find('span', class_='matches__date').text.strip()

time = datetime.strptime(time, '%H:%M').strftime('%I:%M %p')
#change from gmt to ist
time = datetime.strptime(time, '%I:%M %p') + timedelta(hours=5, minutes=30)
time = time.strftime('%I:%M %p')
current_time = datetime.now()
#check if current time is 6 hours behind the match time
message = f"{team_name}'s next match is against " + team + " on " + date + " at " + time + " in the " + comp
toast("MATCHDAY ⚽",message)


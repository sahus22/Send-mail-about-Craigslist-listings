import requests
from bs4 import BeautifulSoup
import smtplib
n=smtplib.SMTP('smtp.gmail.com',587)
n.starttls()
n.ehlo()
n.login('sendersemail8@gmail.com','forsending')
x="metal gear"
url = 'https://newyork.craigslist.org/search/sss?query='+str(x)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
y=""
for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
    href = "https://newyork.craigslist.org" + link.get('href')
    title = link.string
    y=y+str(title)+"\t"+str(href)+"\n"
y = y.encode('ascii', 'ignore').decode('ascii')
n.sendmail('sendersemail8@gmail.com','sendersemail8@gmail.com',"Subject:"+str(x)+" listings in Craigslist New York\n\n"+y)
print('mail sent to\nemail:sendersemail8@gmail.com\npassword:forsending')
n.quit()
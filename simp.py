import requests
from bs4 import BeautifulSoup

url = ("https://brocadeofficial.com/collections/tshirts")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# extract introduction, data processing
tshirts = soup.find_all('div', class_='group relative flex h-full flex-col text-center hover:text-scheme-accent')
for tshirt in tshirts: 
    
    tshirt_name = tshirt.find('div', class_= 'text-center break-word').text
    price = tshirt.find('div', class_= 'text-center mt-1').text
    print(f'''
        tshirt name:{tshirt_name}
        price of the tshirt:{price}
        ''')
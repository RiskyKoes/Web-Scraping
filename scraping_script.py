import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Bagian yang menggunakan BeautifulSoup dan Requests
url = 'https://shopee.co.id'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Periksa apakah tag <title> ditemukan sebelum mencoba mengakses propertinya
if soup.title and soup.title.text:
    title = soup.title.text
    print(f'BeautifulSoup Title: {title}')
else:
    print('Title not found on the page.')

# Bagian yang menggunakan Selenium
# Dapatkan path ke direktori proyek saat ini
project_directory = os.path.dirname(os.path.abspath(__file__))

# Gabungkan path ke ChromeDriver
chrome_driver_path = os.path.join(project_directory, 'chromedriver')

# Opsi Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Opsional: menjalankan browser dalam mode tanpa kepala

# Inisialisasi WebDriver menggunakan path ke ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
selenium_title = driver.title
print(f'Selenium Title: {selenium_title}')

# Ekstraksi Informasi Produk dengan BeautifulSoup
product_containers = soup.find_all('div', class_='col-xs-2-4 shopee-search-item-result__item')
for container in product_containers:
    product_name = container.find('div', class_='yQmmFK _1POlWt _36CEnF').text
    product_price = container.find('span', class_='WTFwws _1lK1qi _1YoBfV').text
    print(f'Product: {product_name}, Price: {product_price}')

# Tutup WebDriver
driver.quit()

from selenium import webdriver
import time

browser = webdriver.Chrome() # Tarayicimizi Chrome Olarak Belirliyoruz

url = "http://lezzetlisunumlarim.com/?Page=" # Internet Sitemizin Adresi

pageNumber = 1 # Sitemizdeki Sayfalarda 5 Yazi Oldugu İcin Sureki Olarak Artacak Degisken
headlines = []
headlineNumber = 1

# Toplam 4 Sayfamiz Oldugu Icin 1.Sayfadan Baslayip 4.Sayfaya Kadar Gidecek Ve Basliklari Ekrana Yazdiracak
while pageNumber<=4:
    newUrl = url + str(pageNumber)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector(".card-title") # Basliklarimiz Card-Title Classının Icinde Oldugu Icin Bu Yontemi Kullaniyoruz
    for element in elements:
        headlines.append(element.text)
    time.sleep(2) # Her Sayfa Icin 2 Saniye Bekleme Suremiz Var
    pageNumber += 1

with open("headlines.txt","w",encoding="UTF-8") as file: # headlines.txt Adinda Bir Dosya Olusturuyoruz Ve Yazdirma Islemini Buraya Yapiyoruz
    for line in headlines:
        file.write(str(headlineNumber) + " " + line + "\n")
        headlineNumber += 1

browser.close() # Tarayicimizi Kapatiyoruz          
  

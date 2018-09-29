from selenium import webdriver
import time

browser = webdriver.Chrome() # Tarayicimizi Belirledik

url = "http://lezzetlisunumlarim.com/Uye/Login/" # Gidecegimiz Url Adresini Belirledik

browser.get(url) # Url Adresini Actik

time.sleep(2) # 2 Saniye Bekledik

username = browser.find_element_by_id("KULLANICIADI") # Kullanici Adi Kismini Bulduk
password = browser.find_element_by_id("SIFRE") # Sifre Kismibi Bulduk

username.send_keys(" Kullanici Adi Buraya Yazilacak ") # Kullanici Adi Kismina Kullanici Adi Degerini Gonderdik
password.send_keys(" Sifre Buraya Yazilacak ") # Sifre Kismina Sifre Degerini Gonderdik

xlogin = "/html/body/div[2]/div/div[1]/form/div[1]/div[3]/div/input" # Giris Yap Butonunun XPath Yolunu Aldik

login = browser.find_element_by_xpath(xlogin) # Giris Yap Butonunu Bulduk Ve Degerini Gonderdik

login.click() # Giris Yap Butonuna Tikladik

time.sleep(3) # 3 Saniye Bekledik

browser.close() # Tarayicimizi Kapattik



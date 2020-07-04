from selenium import webdriver
import names,random,time
kaçhesapyapalım = int(input("Kaç Hesap Oluşturalım : "))
print("Sistem Başlatılıyor")
print("Mail Hizmeti Başlatılıyor")
tempmailoptions = webdriver.ChromeOptions()
tempmailoptions.add_argument("--incognito")
tempmailoptions.add_argument("--headless")
tempchrome = webdriver.Chrome(options=tempmailoptions)
tempchrome.get("https://smailpro.com/tool/tempmail")
time.sleep(1)
tempchrome.find_element_by_xpath("/html/body/div/main/div/div[2]/div[1]/div[1]/fieldset/div[9]/input").click()
print("41Mail Hizmeti Hazır")
for x in range(1,kaçhesapyapalım + 1):
    print("------------", str(x) + ". Hesap Oluşturuluyor ---------------------")
    ourname = names.get_full_name()
    userid = names.get_first_name() + str(random.randint(100000, 99999999))
    şifre = str(random.randint(1000000, 9999999))
    mail = userid + "@stempmail.com"
    print("Mail Ayarlanıyor")
    tempchrome.find_element_by_xpath("/html/body/div/main/div/div[2]/div[1]/div[2]/fieldset/div/input").send_keys(
        userid)
    tempchrome.find_element_by_xpath("/html/body/div/main/div/div[3]/div[2]/div/button").click()
    time.sleep(1)
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(options=chrome_options)
    print("Üyelik Formu Ayarlanıyor")
    chrome.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(8)
    print("Bilgiler Giriliyor")
    try:
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(
            mail)  # MAİL ADRES
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input").send_keys(ourname)
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input").send_keys(userid)
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input").send_keys(şifre)
        time.sleep(2)
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button").click()
        time.sleep(5)
    except:
        print("Hata Oldu Bir Sonraki Hesaba Geçiliyor")
        chrome.close()
        chrome.quit()
        continue
    print("Yaş Doğrulaması Geçiliyor")
    chrome.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[45]").click()
    chrome.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[15]").click()
    time.sleep(3)
    chrome.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button").click()
    time.sleep(5)
    print("Mail Onayı Bypass Ediliyor")
    print("Mail Bekleniyor")
    chrome.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/article/div/div[1]/div/div[2]/div/button").click()
    time.sleep(40)
    tempchrome.find_element_by_xpath("/html/body/div/main/div/div[4]/div/div/div[1]/div[2]/div[2]/button").click()
    time.sleep(3)
    print("Mail Geldi")
    elem = tempchrome.find_elements_by_xpath('.//span[@class = "font-weight-light"]')[0]
    if str(elem.text).endswith("is your Instagram code"):
        print("Mail Onay Kodu : " + str(elem.text)[0:6])
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/div[3]/form/div[1]/input").send_keys(
            str(elem.text)[0:6])
        time.sleep(2)
        chrome.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/div[3]/form/div[2]/button").click()
        time.sleep(2)
        print("Hesap Oluşturuldu")
        print("Kalıntılar Temizleniyor")
        print(userid + ":" + şifre + "\n")
        print("hesaplar.txt ye Kaydediliyor")
        tempchrome.refresh()
        time.sleep(2)
        open("hesaplar.txt", "a").write(userid + ":" + şifre + "\n")
        chrome.close()
        chrome.quit()
        print("Sonraki İşleme Geçiliyor")

print("İşlemler Bitti")
print("Tüm Kalınıtılar Temizleniyor")
tempchrome.close()
tempchrome.quit()
print("Toplam Açılan Hesap Sayısı :" , str(kaçhesapyapalım))
print("Script By Furkan")
print("instagram : f.urkan7")
input("Çıkmak için entera bas")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver'ı başlat
chrome_options = Options()
chrome_options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştır
service = Service('C:/Users/ryntm/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=service)
# Web sayfasının URL'si
url = 'https://www.sikayetvar.com/ulker'

# Sayfayı aç
driver.get(url)

# Sayfanın dinamik olarak yüklenmesini bekle
try:
    # CSS seçicisini güncellemen gerekebilir
    review_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.complaint-description'))
    )

    # İnceleme metinlerini çıkart
    review_content = [review.get_attribute('textContent').strip() for review in review_elements]

    print(review_content)

finally:
    # Tarayıcıyı kapat
    driver.quit()

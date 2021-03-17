from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import selenium.webdriver.support.expected_conditions as EC


class MobilePage:
    MOBILE_INPUT = (By.NAME, '1213-abonentCode')
    CHECK_BUTTON = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div/div[2]/form/button/span/span')
    SELECT_SERVICE = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/label')
    SERVICE_ADD_BALANCE = (By.XPATH, '//*[@id="BONUS"]/a[@title="ბალანსის შევსება"]')
    SERVICE_METI8 = (By.XPATH, '//*[@id="BONUS"]/a[contains(@title,"მეტი") and contains(@title,"8")]')
    SERVICE_METI10 = (By.XPATH, '//*[@id="BONUS"]/a[contains(@title,"მეტი") and contains(@title,"10")]')

    DAVALIANEBA = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[1]/small/span')
    DAVALIANEBA_VALUE = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[1]/p')
    TANXIS_ODENOBA = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[2]/small/span[1]')
    TANXIS_ODENOBA_VALUE = (By.NAME, '1327')

    COMISSION = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[3]/div[1]/button/small/span')
    COMISSION_VALUE = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[1]/div[3]/div[2]/button/span[1]')

    JAMSHI_GADASAXDELI = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/small/span')
    JAMSHI_GADASAXDELI_VALUE = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/b')
    GADAXDA = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/button[2]/span')

    def __init__(self, browser):
        self.browser = browser

    def search(self, mobile_number):
        search_input = self.browser.find_element(*self.MOBILE_INPUT)
        search_input.send_keys(mobile_number)
        self.browser.find_element(*self.CHECK_BUTTON).click()


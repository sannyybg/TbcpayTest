from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
import selenium.webdriver.support.expected_conditions as EC


class TbcPayMainPage:
    URL = 'https://tbcpay.ge/'
    SEARCH_INPUT = (By.NAME, 'searchWord')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div/div/form/button/i')

    SERVICES = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[2]/span')
    TRANSFERS = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[3]/span')
    FOR_BUSINESS = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[4]/span')
    FOREIGN_PAYMENTS = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav/a[5]/span')

    POPULAR_SERVICES = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[1]/a/div[2]/span[1]')
    MOBILURI_KAVSHIRI = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[2]/a/div[2]/span[1]')
    BANKEBI_DAZGVEVA_MIKRO = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[3]/a/div[2]/span[1]')
    TOTALIZATORI_KAZINO = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[4]/a/div[2]/span[1]')
    INTERNETI_TELEFONI_TV = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[5]/a/div[2]/span[1]')
    KOMUNALURI = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[6]/a/div[2]/span[1]')
    TRANSPORTI = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[7]/a/div[2]/span[1]')
    SAXELMWIFO_GADASAXADEBI = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[8]/a/div[2]/span[1]')
    SXVADASXVA = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul/li[9]/a/div[2]/span[1]')

    MOBILURI_BALANSIS_SHEVSEBA = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div/ul/li[2]/a/div/strong')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)



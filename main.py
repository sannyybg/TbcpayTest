from webbrowser import Chrome

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from pages.main_page import TbcPayMainPage
from pages.mobile_page import *

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()



def check_element_existence(browser, element):
    wait(browser, 10).until(EC.presence_of_element_located(element))
    return True

@allure.severity(allure.severity_level.NORMAL)
def test_check_menu_elements(browser):
    tbc_page = TbcPayMainPage(browser)
    tbc_page.load()
    assert check_element_existence(browser, tbc_page.SERVICES) is True
    assert check_element_existence(browser, tbc_page.TRANSFERS) is True
    assert check_element_existence(browser, tbc_page.FOR_BUSINESS) is True
    assert check_element_existence(browser, tbc_page.FOREIGN_PAYMENTS) is True
    assert check_element_existence(browser, tbc_page.POPULAR_SERVICES) is True
    assert check_element_existence(browser, tbc_page.MOBILURI_KAVSHIRI) is True
    assert check_element_existence(browser, tbc_page.BANKEBI_DAZGVEVA_MIKRO) is True
    assert check_element_existence(browser, tbc_page.TOTALIZATORI_KAZINO) is True
    assert check_element_existence(browser, tbc_page.INTERNETI_TELEFONI_TV) is True
    assert check_element_existence(browser, tbc_page.KOMUNALURI) is True
    assert check_element_existence(browser, tbc_page.TRANSPORTI) is True
    assert check_element_existence(browser, tbc_page.SAXELMWIFO_GADASAXADEBI) is True
    assert check_element_existence(browser, tbc_page.SXVADASXVA) is True
    allure.attach(browser.get_screenshot_as_png(), name="mainMenuScreen", attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.MINOR)
def test_check(browser):
    tbc_page = TbcPayMainPage(browser)
    tbc_page.load()


    tbc_page.search("მობილური")
    assert check_element_existence(browser, tbc_page.MOBILURI_BALANSIS_SHEVSEBA) is True
    browser.find_element(*tbc_page.MOBILURI_BALANSIS_SHEVSEBA).click()

    mobile_page = MobilePage(browser)
    assert check_element_existence(browser, mobile_page.MOBILE_INPUT) is True
    assert check_element_existence(browser, mobile_page.CHECK_BUTTON) is True

    mobile_page.search("555122334")

    browser.find_element(*mobile_page.SELECT_SERVICE).click()
    assert check_element_existence(browser, mobile_page.SERVICE_ADD_BALANCE) is True
    assert check_element_existence(browser, mobile_page.SERVICE_METI8) is True
    assert check_element_existence(browser, mobile_page.SERVICE_METI10) is True

    browser.find_element(*mobile_page.SERVICE_METI10).click()

    assert check_element_existence(browser, mobile_page.DAVALIANEBA) is True
    assert browser.find_element(*mobile_page.DAVALIANEBA_VALUE).text == "10.00 c"
    assert check_element_existence(browser, mobile_page.TANXIS_ODENOBA) is True
    assert browser.find_element(*mobile_page.TANXIS_ODENOBA_VALUE).get_attribute("value") == "10"
    assert check_element_existence(browser, mobile_page.COMISSION) is True
    assert browser.find_element(*mobile_page.COMISSION_VALUE).text == "0.12"
    assert check_element_existence(browser, mobile_page.JAMSHI_GADASAXDELI) is True
    assert browser.find_element(*mobile_page.JAMSHI_GADASAXDELI_VALUE).text == "10.12 c"
    assert check_element_existence(browser, mobile_page.GADAXDA) is True
    browser.find_element(*mobile_page.GADAXDA).click()

    wait(browser, 10).until(EC.url_contains("ecommerce.ufc.ge"))
    allure.attach(browser.get_screenshot_as_png(), name="urlScreen", attachment_type=AttachmentType.PNG)



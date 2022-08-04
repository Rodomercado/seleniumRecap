from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.pageindex import *
from pages.pageitemlist import *
from pages.pageitem import *

class Items(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito') #agregar argumento, iniciar en modo incognito
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver.exe', options = chrome_options)
        self.driver.get('http://automationpractice.com/index.php')

    #def test_do_nothing(self):
    #    pass

    def test_view_item_page(self):
        page_index = Page_index(self.driver)
        page_item_list = Page_item_list(self.driver)
        page_item = Page_item(self.driver)
        page_index.search_items('dress')
        page_item_list.click_first_item()
        page_item.verify_text('Printed Summer Dress')
        #self.driver.implicitly_wait(5)
        #self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        #title = self.driver.find_element(By.XPATH, '//h1[@itemprop="name"]').text
        #self.assertEqual(title, 'otra cosa', 'Text should be different')
        #self.assertEqual(title, 'Printed Summer Dress', 'Text should be different')

    def test_search_with_no_items(self):
        page_index = Page_index(self.driver)
        page_index.search_items('computer')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
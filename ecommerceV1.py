from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class Items(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')

    def test_do_nothing(self):
        pass

    def test_view_item_page(self):
        self.driver.find_element(By.ID, "search_query_top").send_keys('dress')
        self.driver.find_element(By.NAME, "submit_search").click()
        self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



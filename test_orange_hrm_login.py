from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
import os
class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title did not match")
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.assertEqual()("OrangeHRM", self.driver.title, "webpage title did not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed......")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= os.getcwd() + "\\Reports"))
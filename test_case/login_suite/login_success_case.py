import os
import unittest
import time
import HTMLTestRunnner
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.HTMLTestRunner import HTMLTestRunner

# current = os.path.dirname(__file__)
# chrome_driver_path = os.path.join(current,'../webdriver/chromedriver')

current = os.path.dirname(__file__)
foxfire_driver_path = os.path.join(current,'../../webdriver/geckodriver')

class ZentaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=foxfire_driver_path)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/zentao/my/')

    def tearDown(self):  #测试清理  浏览器关闭 注册
        time.sleep(2)
        self.driver.quit()

    def test_login_1(self):
        '''case01 使用admin zentao123 测试能否登录禅道'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('zentao123')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        actual_result = self.driver.find_element(By.XPATH,'//span[class="user_name"]').text
        self.assertEqual(actual_result,'admin','test_login_1用例执行失败')

    def test_login_2(self):
        '''case02 使用hm01 123456 测试能否登录禅道'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('hm01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        actual_result = self.driver.find_element(By.XPATH,'//span[@class="username"]').text
        self.assertEqual(actual_result,'黑猫01','test_login_2用例执行失败')


if __name__ == '__main__':
    suite01 = unittest.TestSuite(unittest.makeSuite(ZentaoTest))
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = open('result_%s.html' % now_time,'wb')
    html_runner = HTMLTestRunnner.HTMLTestRunnner(stream=fp,
                                                  title='禅道UI自动化测试报告',
                                                  description='执行用例的测试报告')
    html_runner.run(suite01)

    unittest.main(verbosity=2)



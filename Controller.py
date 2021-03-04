from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class Controller:
    def __init__(self):
        self.driver = self.get_driver()

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_extension("1.3.0_0.crx")
        new_driver = webdriver.Chrome(options=options)
        return new_driver

    def navigate_alphabetically(self):
        for letter1iterator in range(8, 26):
            for letter2iterator in range(0, 26):
                letter1 = chr(ord('a') + letter1iterator)
                letter2 = chr(ord('a') + letter2iterator)
                domain = letter1 + letter2 + ".com"
                try:
                    self.driver.get("http://" + domain)
                    self.driver.get_screenshot_as_file(domain + ".png")
                except WebDriverException:
                    print("Page down: " + domain)

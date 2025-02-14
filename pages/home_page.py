from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    PERFUME_MENU = (By.XPATH, "//a[normalize-space()='PARFUM']")

    def accept_cookies(self):

        try:

            shadow_host = self.driver.find_element(By.CSS_SELECTOR,
                                                   "#usercentrics-root")
            shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)

            accept_button = shadow_root.find_element(By.CSS_SELECTOR, ".sc-dcJsrY.eIFzaz")

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(accept_button))
            accept_button.click()
            print("Accept Cookies button clicked successfully!")

        except Exception as e:
            print(f"Unable to click Accept Cookies button: {e}")

    def __init__(self, driver):
        super().__init__(driver)


    def navigate_to_perfume(self):

        self.click_element(self.PERFUME_MENU)
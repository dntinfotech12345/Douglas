from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PerfumePage:

    def __init__(self, driver):
        self.driver = driver

    MAKE_FILTER_DROPDOWN = (By.XPATH, "div[class='facet__title'][data-testid='brand']")
    CHECKBOX_ANCHOR_TAGS = (By.XPATH, "//div[@class='facets-wrapper']//a")

    def select_make_filters(self, make_filters):

        try:

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.MAKE_FILTER_DROPDOWN)
            ).click()


            checkbox_anchors = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.CHECKBOX_ANCHOR_TAGS)
            )


            for make in make_filters:
                for anchor in checkbox_anchors:
                    checkbox = anchor.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
                    label = anchor.text.strip()

                    if label == make and not checkbox.is_selected():
                        checkbox.click()
                        print( "Selected filter: {make}")
                        break

        except Exception as e:
            print(f"Error selecting filters: {e}")

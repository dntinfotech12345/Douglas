import os

class Config:

    BASE_URL = "https://www.douglas.de/de"

    BROWSER = "chrome"
    HEADLESS_MODE = False

    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_DATA_PATH = os.path.join(BASE_DIR, "test_data", "test_data.xlsx")

    ENABLE_ALLURE_REPORT = True

    LOG_LEVEL = "INFO"

    ACCEPT_COOKIES = True


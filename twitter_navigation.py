import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from secrets import bot_pass, bot_email
from bot_logic import Bot


# Main class for bot
class LoginPath:

    # Initialise variables
    def __init__(self, post):
        self.twitter_login_url = "https://twitter.com/login"
        self.post = post

        # Set the settings of the browser
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)

        # Create the driver
        self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe", chrome_options=self.chrome_options)

        # Find chrome in path
        self.driver.get(self.twitter_login_url)

    # Function to log in the bot
    def login(self):

        # Get an element from the page
        login_area = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                          ((By.NAME, "session[username_or_email]")))
        password_area = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                             ((By.NAME, "session[password]")))
        
        # Set the text of the login and pass
        login_area.send_keys(bot_email)
        password_area.send_keys(bot_pass)

        # Login
        password_area.send_keys(Keys.ENTER)

    # Post a tweet to twitter
    def make_post(self):

        # Login to twitter
        self.login()

        # Select the tweet area
        autotw1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
        autotw1.click()

        # Enter the tweet into the tweet area and then post it
        element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
        ActionChains(self.driver).move_to_element(element).send_keys(self.post).key_down(Keys.CONTROL)\
            .send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()


# Initial testing
if __name__ == "__main__":
    LoginPath(Bot().generate_a_post()).make_post()

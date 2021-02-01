import time
from random import randint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Main class
class Bot:

    # Initialise variables
    def __init__(self):

        # List of potential moods
        choices = ["happy", "angry", "sad", "chilled", "inspirational"]

        # Select a random mood
        self.mood = choices[randint(0, len(choices) - 1)]

        # Link to the google driver
        self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
        self.text = None

    # Convert tweet to broken english
    def covert_to_broken_english(self, convert_value):

        # Get the website
        self.driver.get("https://lingojam.com/BadTranslator")

        # Get the cookies tab and accept it
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             ((By.CLASS_NAME, "css-flk0bs"))).click()

        # Get the text input area and place the tweet into it to be converted
        convert_to_broken_english = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                                         ((By.XPATH, "//textarea[@id='english-text']")))
        convert_to_broken_english.clear()
        convert_to_broken_english.send_keys(convert_value)

        # Wait for the textarea value to be updated
        time.sleep(4)

        # Get the value of the broken english text box and then return it as long as it isn't linger than 260 chars
        get_bad_english = self.driver.find_element_by_xpath("//div[2]/div/textarea").get_attribute("value")
        if len(get_bad_english) < 250:
            return get_bad_english
        else:
            return get_bad_english[:260]

    # Find a random comment on twitter
    def get_a_random_comment(self, url):

        # Get the twitter page
        self.driver.get(url)

        # Get the first tweet on the page and open it
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             ((By.XPATH,
                                               "//div[@id='react-root']/div/div/div[2]/main/div/div/div/div"
                                               "/div/div[2]/div/div/section/div/div/div/div/div/article/div/"
                                               "div/div/div[2]/div"))).click()

        # Get the text content of the tweet
        self.text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[3]/div/div/"
                                                                                                   "div/span"))).text

        # Check to make sure that the tweet is longer than 15 chars and mas more than 2 words in it, if not then rerun
        # the whole function after a wait time of 4 seconds
        if len(self.text) < 15 and len(self.text.split(" ")) < 2:
            time.sleep(4)
            return self.get_a_random_comment(url)

        # Return the broken english tweet and add 2 hash_tags from the given text
        final_tweet = self.covert_to_broken_english(self.text)
        hash_tags = final_tweet.split(' ')
        return f"{str(final_tweet)}\n#{hash_tags[randint(0, len(hash_tags) - 1)]} #" \
               f"{hash_tags[randint(0, len(hash_tags) - 1)]}"

    # Determine where to get the tweet from based on the random mood of the bot
    def generate_a_post(self):
        if self.mood == "happy":
            return self.get_a_random_comment\
                ("https://twitter.com/search?q=happy&src=typed_query&f=live")
        elif self.mood == "angry":
            return self.get_a_random_comment\
                ("https://twitter.com/search?q=angry&src=typed_query&f=live")
        elif self.mood == "sad":
            return self.get_a_random_comment\
                ("https://twitter.com/search?q=sad&src=typed_query&f=live")
        elif self.mood == "chilled":
            return self.get_a_random_comment\
                ("https://twitter.com/search?q=chillin&src=typed_query&f=live")
        else:
            return self.get_a_random_comment\
                ("https://twitter.com/search?q=motivation&src=typed_query&f=live")

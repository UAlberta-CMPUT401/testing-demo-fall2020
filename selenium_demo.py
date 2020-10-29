from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

# Navigate to site
driver.get("https://google.ca")

# After inspecting the page, we see the search bar resides in an element named q
elem = driver.find_element_by_name("q")
assert elem != None

#Enter a search term
elem.send_keys("UAlberta")
elem.send_keys(Keys.RETURN)

driver.quit()

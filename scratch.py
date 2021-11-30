import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


youtube_trending_url = "https://www.youtube.com/feed/trending"


def get_driver():
  chrome_options = Options()
  chrome_options.binary_location = '/opt/headless-chromium'
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--single-process')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

if __name__ == "__main__":

  print("Creating Driver")
  driver = get_driver()

  print("Fetching the Page")
  driver.get(youtube_trending_url)

  print("Get the Video's Div's")
  Video_Div_Class_Name = 'ytd-video-renderer'
  video_divs = driver.find_elements_by_class_name(Video_Div_Class_Name)

  print(f'Found {len(video_divs)} Videos')

# response = requests.get(youtube_trending_url)

# print('Status Code', response.status_code)

# with open ("trading.html", "w") as f:
#   f.write(response.text)

# doc = BeautifulSoup(response.text, "html.parser")

# print("Page Title:", doc.title)

# video_divs = doc.find_all('div', class_='ytd-video-renderer')

# print(f'Found {len(video_divs)} Videos')

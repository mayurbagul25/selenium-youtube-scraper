from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


youtube_trending_url = "https://www.youtube.com/feed/trending"


def get_driver():
  chrome_options = Options()
  # chrome_options.binary_location = '/opt/headless-chromium'
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--single-process')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  driver.get(youtube_trending_url)
  Video_Div_Class_Name = 'ytd-video-renderer'
  video_divs = driver.find_elements(By.TAG_NAME, Video_Div_Class_Name)
  return video_divs

if __name__ == "__main__":

  print("Creating Driver")
  driver = get_driver()

  print("Fetching the Page")
  videos = get_videos(driver)
  
  print(f'Found {len(videos)} Videos')

  print('Parsing first Video')

  video = videos[0]
  
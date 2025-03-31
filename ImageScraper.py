from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import requests
# Automatically download the correct driver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Update the  here too
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "", 
}

print("Chrome WebDriver is working!")
folder_name = input("enter folder name")  

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

image_url = input("enter the img url")
pic_num_count = 0


driver.get(image_url)
time.sleep(5)  # Wait for JS to load (adjust as needed)

    # Find image links
thumbnails = driver.find_elements(By.CSS_SELECTOR, ".thumb a")
href_links = [a.get_attribute("href") for a in thumbnails]
    
for links in href_links:
    driver.get(links)
    time.sleep(2)
        
    try:
        img = driver.find_element(By.ID, "image")
        download_img_url = img.get_attribute("src")
        print(download_img_url)
            
            # Download the image
        with open(os.path.join(folder_name, f"{folder_name}{pic_num_count}.jpeg"), "wb") as file:
            file.write(requests.get(download_img_url, headers=headers).content)
            time.sleep(1) 
                
        print(f"Downloaded {pic_num_count + 1} picture")
        pic_num_count += 1
    except:
        print("Failed to find image")
        
print("Done")
driver.quit()

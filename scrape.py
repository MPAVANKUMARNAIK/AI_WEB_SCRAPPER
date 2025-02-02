from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time

USERNAME = 'toparamsrenitha_3ES6hK'
ACCESS_KEY = 'z6HkXTp2GYwzVTuh7XZp'
BROWSERSTACK_URL = f'https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

def scrape_website(website):
    print("Launching chrome browser...")

    desired_cap = {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'name': 'Sample Test',  # Test name
        'browserstack.debug': 'true'  # Enable debugging on BrowserStack
    }

    options = webdriver.ChromeOptions()
    for key, value in desired_cap.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        driver.get(website)
        
        # Adjust the wait time for CAPTCHA solving or loading
        print("Waiting briefly for CAPTCHA or content load...")
        time.sleep(5)  # Adjust based on your observations
        
        print('Navigated! Scraping page content...')
        html = driver.page_source
    except Exception as e:
        print(f"Error occurred: {e}")
        html = ""
    finally:
        driver.quit()

    return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=60000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]

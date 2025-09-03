"""
Project: Basic Browser Automation for Security Testing
Author: Ravinshu (Cyber Security Student)
Internship: Deltaware Solutions – Penetration Testing Internship

Description:
------------
This script demonstrates a simple use of Python and Selenium
for basic web application security testing.
It performs the following tasks:
1. Opens the target website.
2. Searches for a login form and attempts a dummy login.
3. Captures a screenshot of the page as proof of execution.

Note:
- This is an educational project for internship submission.
- Always use demo/test sites (like DVWA or testphp.vulnweb.com).
"""

# ==============================
# Import Libraries
# ==============================
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ==============================
# Configuration
# ==============================
TARGET_URL = "http://testphp.vulnweb.com"   # Demo site for testing
SCREENSHOT_FILE = "result.png"              # Screenshot filename

# ==============================
# Launch Browser
# ==============================
print("[+] Starting browser...")
driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
driver.maximize_window()

# Open target site
print(f"[+] Opening website: {TARGET_URL}")
driver.get(TARGET_URL)
time.sleep(2)

# ==============================
# Try Login Form (if available)
# ==============================
try:
    username = driver.find_element(By.NAME, "uname")
    password = driver.find_element(By.NAME, "pass")
    login_btn = driver.find_element(By.NAME, "login")

    username.send_keys("admin")
    password.send_keys("1234")
    login_btn.click()
    time.sleep(2)

    print("[+] Attempted login with test credentials (admin:1234)")
except:
    print("[-] No login form found on this page")

# ==============================
# Save Screenshot
# ==============================
driver.save_screenshot(SCREENSHOT_FILE)
print(f"[+] Screenshot saved as {SCREENSHOT_FILE}")

# ==============================
# Close Browser
# ==============================
driver.quit()
print("[+] Test completed successfully")


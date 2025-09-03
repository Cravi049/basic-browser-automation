# Basic Browser Automation for Security Testing

## 📌 Overview
This is a simple cybersecurity project built during my Penetration Testing Internship at **Deltaware Solutions**.  
The goal of this project is to automate basic web security testing tasks using **Python + Selenium**.

The script simulates a human tester by:
- Opening a website automatically.
- Checking for a login form and attempting a test login with dummy credentials.
- Capturing a screenshot of the page as proof of execution.

This project is beginner-friendly and shows the use of **Python in security automation**.

---

## 🛠 Tools & Technologies Used
- Python 3
- Selenium (for browser automation)
- ChromeDriver

---

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/basic-browser-automation.git
   cd basic-browser-automation
2. install Selenium
      ```pip install selenium``` or ```pip3 install selenium ```if the error is occure then "```pip3 install selenium --break-system-packages```" - This tells Kali “yes, I know, still install it globally.”
3. Verify Installation
   ```pip show selenium``` or ```pip3 show selenium```

4. Download and set up ChromeDriver:

     -Download ChromeDriver
     -Place it in your PATH.
5. Run the script:
     ```python
   python main.py
   
     ```python
     python3 main.py
6. Output:

     -A screenshot will be saved as result.png.

     -Terminal output will confirm steps.

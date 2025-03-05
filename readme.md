# Selenium Automation Testing Project

## Overview

This project demonstrates **automated UI testing** using **Selenium WebDriver and Python**. It includes test cases for:

- **Login Authentication** – Automates login verification on a practice website.
- **Form Validation** – Tests input validation on an HTML form.
- **UI Elements Verification** – Ensures critical UI elements are present on a webpage.

## Prerequisites

Ensure you have the following installed:

- **Python (3.x)**
- **Google Chrome Browser**
- **Chrome WebDriver** (Download from [here](https://sites.google.com/chromium.org/driver/))
- **Selenium Library** (Install using `pip install selenium`)


This will:

- Open a browser and test the **login page**.
- Validate the **form input**.
- Check for essential **UI elements**.

## Test Cases

### 1. Login Authentication Test

- Opens [Practice Test Login](https://practicetestautomation.com/practice-test-login/).
- Enters **valid credentials** (`student / Password123`).
- Clicks **Submit** and verifies login success.

### 2. Form Validation Test

- Opens [W3Schools Form Page](https://www.w3schools.com/html/html_forms.asp).
- Enters an **invalid email** in the name field.
- Clicks submit and verifies the expected behavior.

### 3. UI Elements Verification

- Opens [Practice Test Automation](https://practicetestautomation.com/).
- Checks if "Practice" and "Test Login Page" links exist.

## Expected Output

If all tests pass, the script will execute without errors. If a test fails, it will throw an assertion error.


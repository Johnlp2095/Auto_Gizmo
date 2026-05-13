from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_correct_answer(question_text):
    """
    Determine the correct answer from the question text.
    TODO: Implement your answer-finding logic here:
    - Use Google search API
    - Use ChatGPT/Claude API
    - Have a hardcoded Q&A dictionary
    - Use another method
    """
    # Placeholder - return empty to skip for now
    return ""

def login_to_gizmo(driver):
    """Auto-login to Gizmo using credentials from .env"""
    email = os.getenv("GIZMO_EMAIL")
    password = os.getenv("GIZMO_PASSWORD")
    
    if not email or not password:
        print("⚠️  ERROR: GIZMO_EMAIL or GIZMO_PASSWORD not set in .env file")
        return False
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # Click sign in button if visible
        try:
            sign_in_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in') or contains(text(), 'Login')]")
            driver.execute_script("arguments[0].click();", sign_in_btn)
            print("✓ Clicked Sign In button")
            time.sleep(2)
        except:
            pass
        
        # Enter email
        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_field.clear()
            email_field.send_keys(email)
            print("✓ Entered email")
            time.sleep(1)
        except Exception as e:
            print(f"Could not find email field: {e}")
            return False
        
        # Enter password
        try:
            password_field = driver.find_element(By.NAME, "password")
            password_field.clear()
            password_field.send_keys(password)
            print("✓ Entered password")
            time.sleep(1)
        except Exception as e:
            print(f"Could not find password field: {e}")
            return False
        
        # Click login button
        try:
            login_btn = driver.find_element(By.XPATH, "//*[@type='submit' or contains(text(), 'Sign in') or contains(text(), 'Login')]")
            driver.execute_script("arguments[0].click();", login_btn)
            print("✓ Clicked Login")
            time.sleep(3)
        except Exception as e:
            print(f"Could not find login button: {e}")
            return False
        
        # Wait for page to load after login
        time.sleep(3)
        print("✓ Login successful!")
        return True
    
    except Exception as e:
        print(f"Login error: {e}")
        return False

def navigate_to_quiz():
    """Navigate through the Gizmo setup flow"""
    # Use fresh browser without profile to avoid school redirect issues
    options = webdriver.EdgeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--inprivate")  # InPrivate/Incognito mode
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    try:
        driver = webdriver.Edge(options=options)
    except Exception as e:
        print(f"Error: Could not start Edge browser")
        print(f"Error details: {e}")
        return None
    
    email = os.getenv("GIZMO_EMAIL")
    password = os.getenv("GIZMO_PASSWORD")
    
    if not email or not password:
        print("⚠️  ERROR: GIZMO_EMAIL or GIZMO_PASSWORD not set in .env file")
        return None
    
    try:
        print("Opening sign-up page...")
        driver.get("https://app.gizmo.ai/sign-up?redirect_url=%2Fdecks%2F79720949")
        time.sleep(2)
        print("yummers")
        wait = WebDriverWait(driver, 10)
        
        # Click "Sign up with email"
        try:
            print("Looking for 'Sign up with email' button...")
            buttons = driver.find_elements(By.TAG_NAME, "button")
            signup_email_btn = None
            
            for btn in buttons:
                btn_text = btn.text.strip()
                if "email" in btn_text.lower() and btn.is_displayed():
                    signup_email_btn = btn
                    print(f"Found button: {btn_text}")
                    break
            
            if signup_email_btn:
                driver.execute_script("arguments[0].scrollIntoView(true);", signup_email_btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", signup_email_btn)
                print("✓ Clicked 'Sign up with email'")
                time.sleep(5)  # Give form time to render
            else:
                print("Could not find 'Sign up with email' button")
        except Exception as e:
            print(f"Error clicking 'Sign up with email': {e}")
        
        # Enter email
        try:
            print("Entering email...")
            all_inputs = driver.find_elements(By.TAG_NAME, "input")
            
            # Find email input by data-testid
            email_field = None
            for inp in all_inputs:
                if inp.get_attribute("data-testid") == "email-input":
                    email_field = inp
                    break
            
            if email_field:
                email_field.click()
                time.sleep(0.5)
                email_field.send_keys(email)
                print("✓ Entered email")
                time.sleep(1)
            else:
                print("Could not find email field")
                return None
        except Exception as e:
            print(f"Error entering email: {e}")
            return None
        
        # Enter password
        try:
            print("Entering password...")
            all_inputs = driver.find_elements(By.TAG_NAME, "input")
            
            # Find password input by data-testid
            password_field = None
            for inp in all_inputs:
                if inp.get_attribute("data-testid") == "password-input":
                    password_field = inp
                    break
            
            if password_field:
                password_field.click()
                time.sleep(0.5)
                password_field.send_keys(password)
                print("✓ Entered password")
                time.sleep(1)
            else:
                print("Could not find password field")
                return None
        except Exception as e:
            print(f"Error entering password: {e}")
            return None
        
        # Click sign up button
        try:
            print("Looking for sign up button...")
            buttons = driver.find_elements(By.TAG_NAME, "button")
            signup_btn = None
            
            for btn in buttons:
                btn_text = btn.text.strip()
                if "sign up" in btn_text.lower() and btn.is_displayed():
                    signup_btn = btn
                    print(f"Found button: {btn_text}")
                    break
            
            if signup_btn:
                driver.execute_script("arguments[0].scrollIntoView(true);", signup_btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", signup_btn)
                print("✓ Clicked Sign Up")
                time.sleep(3)
            else:
                print("Could not find sign up button")
        except Exception as e:
            print(f"Error clicking sign up: {e}")
        
        current_url = driver.current_url
        print(f"Current URL after sign up: {current_url}")
        time.sleep(2)
        
    except Exception as e:
        print(f"Could not complete sign up: {e}")
        driver.quit()
        return None
    
    wait = WebDriverWait(driver, 10)
    
    time.sleep(2)
    print("✓ Ready to navigate Gizmo")
    
    # Click "Study Deck" - Button [0]
    try:
        print("Looking for Study button (index 0)...")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        
        if len(buttons) > 0:
            study_btn = buttons[0]
            print(f"Found button: {study_btn.text.strip()}")
            driver.execute_script("arguments[0].scrollIntoView(true);", study_btn)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", study_btn)
            print("✓ Clicked Study (button 0)")
            time.sleep(2)
        else:
            print("No buttons found")
    except Exception as e:
        print(f"Error clicking Study button: {e}")
        import traceback
        traceback.print_exc()
    
    # Click first "Start Learning" - Button [34]
    try:
        print("Looking for Start Learning button (index 34)...")
        time.sleep(2)  # Extra wait for page to render
        
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Found {len(buttons)} buttons total")
        
        if len(buttons) > 34:
            start_btn = buttons[34]
            print(f"✓ Found button 34: {start_btn.text.strip()}")
            driver.execute_script("arguments[0].scrollIntoView(true);", start_btn)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", start_btn)
            print("✓ Clicked Start Learning (button 34)")
            time.sleep(2)
        else:
            print(f"⚠️  Not enough buttons found (need 34, got {len(buttons)})")
    except Exception as e:
        print(f"Error clicking Start Learning button: {e}")
        import traceback
        traceback.print_exc()
    
    # Click second "Start Learning"
    try:
        print("Looking for second 'Start Learning' button...")
        time.sleep(2)
        
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Found {len(buttons)} buttons total")
        
        # Print all buttons to see what's available
        start_learning_buttons = []
        for i, btn in enumerate(buttons):
            btn_text = btn.text.strip()
            if btn.is_displayed() and "start learning" in btn_text.lower():
                start_learning_buttons.append((i, btn))
                print(f"  Button {i}: {btn_text}")
        
        if len(start_learning_buttons) > 0:
            # Get the last (or first available) Start Learning button
            idx, start_btn = start_learning_buttons[-1] if len(start_learning_buttons) > 1 else start_learning_buttons[0]
            print(f"✓ Found Start Learning at index {idx}: {start_btn.text.strip()}")
            driver.execute_script("arguments[0].scrollIntoView(true);", start_btn)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", start_btn)
            print("✓ Clicked Start Learning (2)")
            time.sleep(3)
        else:
            print("⚠️  Could not find any Start Learning button")
    except Exception as e:
        print(f"Error clicking second Start Learning button: {e}")
        import traceback
        traceback.print_exc()
    
    return driver

def complete_quiz(driver):
    """Answer all quiz questions until round is complete"""
    question_count = 0
    
    while True:
        try:
            # Check if round is complete
            try:
                complete_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Complete')] | //*[contains(text(), 'Round Complete')]")
                print("✓ Round Complete!")
                return True
            except:
                pass
            
            question_count += 1
            print(f"\n--- Question {question_count} ---")
            
            # Try multiple ways to find question text
            question = "Unknown"
            
            # Try different selectors
            selectors = [
                "//*[@class*='question']",
                "//div[@class*='card']",
                "//p[@class*='question']",
                "//h2",
                "//div[contains(@class, 'prompt')]",
            ]
            
            for selector in selectors:
                try:
                    element = driver.find_element(By.XPATH, selector)
                    if element.text and len(element.text) > 0:
                        question = element.text
                        print(f"Found question: {question}")
                        break
                except:
                    continue
            
            if question == "Unknown":
                print("Could not find question text - printing page content...")
                # Print all visible text
                page_text = driver.find_element(By.TAG_NAME, "body").text
                lines = page_text.split("\n")
                for line in lines[:10]:  # Print first 10 lines
                    if line.strip():
                        print(f"  {line}")
            
            # Get answer using your logic
            answer = get_correct_answer(question)
            
            # Try to handle different question types
            
            # Type 1: Click to reveal / Multiple Choice - Click button with matching text
            buttons = driver.find_elements(By.TAG_NAME, "button")
            print(f"Found {len(buttons)} buttons on page")
            
            if buttons:
                print("Available buttons:")
                for i, button in enumerate(buttons):
                    button_text = button.text.strip()
                    if button_text:
                        print(f"  [{i}] {button_text}")
            
            if answer and len(answer) > 0:
                clicked = False
                for button in buttons:
                    button_text = button.text.lower().strip()
                    if answer.lower() in button_text:
                        button.click()
                        print(f"Clicked: {button.text}")
                        clicked = True
                        break
                
                if not clicked and len(buttons) > 0:
                    # If no matching button, try clicking first visible button
                    for button in buttons:
                        if button.is_displayed():
                            button.click()
                            print("Clicked first visible button (no match found)")
                            clicked = True
                            break
            else:
                # No answer found - try clicking first button anyway
                if len(buttons) > 0:
                    for button in buttons:
                        if button.is_displayed():
                            button.click()
                            print("Clicked first visible button (no answer logic)")
                            break
            
            # Type 2: Text input - Find text field and type
            try:
                input_fields = driver.find_elements(By.TAG_NAME, "input")
                if input_fields and answer and len(answer) > 0:
                    for field in input_fields:
                        if field.is_displayed():
                            field.clear()
                            field.send_keys(answer)
                            print(f"Typed: {answer}")
                            # Find and click submit/continue button
                            try:
                                submit_btn = driver.find_element(By.XPATH, "//*[@type='submit'] | //*[contains(text(), 'Next')] | //*[contains(text(), 'Continue')]")
                                submit_btn.click()
                            except:
                                pass
                            break
            except:
                pass
            
            time.sleep(2)
            
        except Exception as e:
            print(f"Error answering question: {e}")
            import traceback
            traceback.print_exc()
            time.sleep(1)

def main():
    driver = None
    try:
        driver = navigate_to_quiz()
        
        # Loop through rounds
        while True:
            print("\n=== STARTING QUIZ ROUND ===")
            complete_quiz(driver)
            
            # Look for "Next Round" button
            try:
                print("Looking for 'Next Round' button...")
                buttons = driver.find_elements(By.TAG_NAME, "button")
                next_round_btn = None
                
                for btn in buttons:
                    btn_text = btn.text.strip()
                    if "Next Round" in btn_text and btn.is_displayed():
                        next_round_btn = btn
                        print(f"Found button: {btn_text}")
                        break
                
                if next_round_btn:
                    driver.execute_script("arguments[0].scrollIntoView(true);", next_round_btn)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", next_round_btn)
                    print("✓ Clicked Next Round")
                    time.sleep(2)
                else:
                    print("No 'Next Round' button found - quiz complete!")
                    break
            except Exception as e:
                print(f"Error looking for Next Round: {e}")
                break
    
    except Exception as e:
        print(f"Fatal error: {e}")
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
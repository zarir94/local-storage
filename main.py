from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_recaptcha import Recaptcha_Solver
from selenium_recaptcha.components import find_until_located, find_until_clicklable
from time import sleep

def interceptor(request):
    request.headers['X-Requested-With'] = 'com.instagram.android'

options=webdriver.ChromeOptions()
# options.headless=True

id='177933481414144'
all_reacts={1:'LIKE',2:'LOVE',3:'HAHA',4:'WOW',5:'SAD',6:'ANGRY'}
react=2

final_react=all_reacts[react]
print(final_react);exit()
driver = webdriver.Chrome(options=options)
driver.set_window_size(400,700)
driver.request_interceptor = interceptor

print('Opening URL')
driver.get("http://cutt.ly/jVtUH4L")

if 'Login Successful' in driver.page_source:
    print('Logged In.')

print('Going Dashboard')
driver.get('http://app.pagalworld2.com/dashboard.php?type=custom')
driver.implicitly_wait(1)

print('Scrolling Down')
driver.execute_script("document.querySelector('.panel').scrollIntoView(true);")
driver.implicitly_wait(1)

print('Solving Captcha')
solver=Recaptcha_Solver(driver)
solver.solve_recaptcha()
print('Captcha Solved')

input_form=find_until_located(driver,By.CSS_SELECTOR, 'input[type=text]')
input_form.send_keys(id)
driver.implicitly_wait(1)
find_until_located(driver, By.CSS_SELECTOR, f'input[type=radio][value={final_react}]').click()
driver.implicitly_wait(1)
find_until_clicklable(driver, By.CSS_SELECTOR, 'input[type=submit]').click()

# driver.save_screenshot('test.png')

driver.implicitly_wait(10*60)

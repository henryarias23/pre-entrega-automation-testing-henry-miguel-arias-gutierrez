#import time
from selenium.webdriver.common.by import By

def login_helper(driver):
    driver.get("https://www.saucedemo.com/")
    #time.sleep(3) lo dejamos en espera 3 segundos
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

#función para reutilizar la acción de agregar producto
def add_product_helper(driver):
    primer_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]
    boton_agregar = primer_item.find_element(By.TAG_NAME, 'button')
    boton_agregar.click()
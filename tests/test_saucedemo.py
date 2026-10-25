from selenium.webdriver.common.by import By
from utils.helpers import login_helper, add_product_helper

def test_01_login (driver):
    login_helper(driver)

    assert "inventory.html" in driver.current_url, "ERROR: no se redirigio a la pagina de inventario"

def test_02_verificar_inventario(driver):
    login_helper(driver)
    tituloPagina = driver.title
    tituloSeccion = driver.find_element(By.CLASS_NAME, "title").text

    assert tituloPagina == "Swag Labs", f'ERROR: Titulo de la ventana esperado"Swag Labs", Obtenido {tituloPagina}'
    assert tituloSeccion == "Products", f'ERROR: Titulo de la ventana esperado"Products", Obtenido {tituloSeccion}'

def test_03_productos_visibles(driver):
    login_helper(driver)
    inventory_item = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(inventory_item) > 0, f'ERROR: No se encontraron productos visibles'
    # [] len() : me muestra el largo de la lista

def test_04_validar_interfaz(driver):
    login_helper(driver)
    botonMenu = driver.find_element(By.ID, 'react-burger-menu-btn')
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')

    assert botonMenu.is_displayed(), f'ERROR: Menu no esta visible'
    assert filtro.is_displayed(), f'ERROR: Filtro no esta visible'

def test_05_añadir_producto_al_carrito (driver):
    login_helper(driver)
    add_product_helper(driver)
    primer_item = driver.find_elements(By.CLASS_NAME,'inventory_item')[0]
    boton_actualizado = primer_item.find_element(By.TAG_NAME, 'button')

    assert boton_actualizado.text.capitalize() == 'Remove', 'ERROR: el boton no cambio a "remove"'

def test_06_verificar_contador_carrito(driver):
    login_helper(driver)
    add_product_helper(driver)
    contadorCarrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text

    assert contadorCarrito == "1", f'ERROR: Se esperaba 1, obtuvo {contadorCarrito}'

def test_07_navegar_carrito(driver):
    login_helper(driver)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    assert "/cart.html" in driver.current_url, 'ERROR: No se dirigio a /cart.html'

def test_08_comprobar_producto_en_el_carrito (driver):
    login_helper(driver)
    add_product_helper(driver) 

    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click() # 2. Vamos al carrito
    producto_nombre_en_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

    assert producto_nombre_en_carrito == 'Sauce Labs Backpack', f'ERROR: No es el mismo nombre'

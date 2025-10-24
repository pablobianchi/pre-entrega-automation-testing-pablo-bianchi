import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time
##para poder utilizar lo que definí dentro de utils
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from utils.helper import login,get_driver,take_screenshot

@pytest.fixture
def driver():
    driver = get_driver();
    
    ##Idea clave
    ##return → devuelve y finaliza la función.
    ##yield → devuelve un valor y suspende la ejecución; la próxima iteración retoma donde quedó.
    yield driver
    driver.quit()




def test_login( driver ):
    login(driver,True)
    assert "/inventory.html" in driver.current_url


def test_inventory(driver:webdriver.Chrome  ):

    login(driver)
    take_screenshot(driver , 'inventario' );

    assert "Swag Labs" in driver.title , f"Título inesperado: {driver.title}"

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0 , f"No se encontraron productos"

    assert len( driver.find_elements(By.CLASS_NAME, 'product_sort_container' ) ) > 0  , f"No se encontró elemento de Orden"

    assert len( driver.find_elements(By.CLASS_NAME, 'bm-burger-button2' ) ) > 0  , f"No se encontró elemento de Menú"


##def test_carrito():
##TODO
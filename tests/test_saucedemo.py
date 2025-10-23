import pytest

##para poder utilizar lo que definí dentro de utils
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from utils.helper import login,get_driver

@pytest.fixture
def driver():
    driver = get_driver();
    
    ##Idea clave
    ##return → devuelve y finaliza la función.
    ##yield → devuelve un valor y suspende la ejecución; la próxima iteración retoma donde quedó.
    yield driver
    driver.quit()


def test_login( driver):
    login(driver)
    assert "/inventory.html" in driver.current_url


##def test_catalogo():


##def test_carrito():
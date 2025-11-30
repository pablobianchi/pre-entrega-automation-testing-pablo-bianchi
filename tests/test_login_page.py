from pages.login_page import LoginPage

from utils.helper import take_screenshot,USERNAME,PASSWORD

def test_login( driver ):

    loginPage = LoginPage( driver )

    loginPage.login_completo(USERNAME,PASSWORD)
    
    take_screenshot(driver , 'login' )

    assert "/inventory.html" in driver.current_url
    
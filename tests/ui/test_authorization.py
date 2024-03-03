import allure
import pytest

from superjob_project.pages.ui.account_page import AccountPage
from superjob_project.pages.ui.base_page import BasePage

account = AccountPage()
base = BasePage()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization of the user")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_create_account():
    with allure.step('Create account'):
        base.registration()
    with allure.step('Check successful registration'):
        base.check_registration()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and response to the vacancy")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
@pytest.mark.xfail(reason="Нестабильный тест")
def test_login_and_response():
    with allure.step('Login in SJ site'):
        base.login()
    with allure.step('Create response to the vacancy'):
        account.create_response()
    with allure.step('Check response'):
        account.check_response()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and create resume")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
@pytest.mark.xfail(reason="Нестабильный тест, динамические окна")
def test_create_resume():
    with allure.step('Login in SJ site'):
        base.login()
    with allure.step('Create resume'):
        account.create_resume()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking the authorization user and close visibility of the resume")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_resume_visibility_off():
    with allure.step('Login in SJ site'):
        base.login()
    with allure.step('Create other resume'):
        account.create_other_resume()
    with allure.step('Close visibility of the resume'):
        account.close_visibility()
    with allure.step('Check visibility of the resume'):
        account.check_visibility()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking base authorization user")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_auth():
    with allure.step('Login in SJ site'):
        base.login()


@allure.epic('Authorized')
@allure.label("owner", "Autohrized user")
@allure.feature("Checking base authorization user and logout")
@allure.tag('ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_logout():
    with allure.step('Login in SJ site'):
        base.login()
    with allure.step('Logout'):
        base.logout()
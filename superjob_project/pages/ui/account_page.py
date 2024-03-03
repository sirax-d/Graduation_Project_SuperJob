import os
import time

from dotenv import load_dotenv
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

from superjob_project.data.ui.users import person, employment, time_w

load_dotenv()
base_url = os.getenv("BASE_URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


class AccountPage:
    def create_resume(self):
        browser.open(base_url + "/user/resume/")
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s(".f-test-button-Sozdat_rezyume").should(be.clickable).click()
        s('[name="person.firstName"]').clear().type(person.first_name)
        s('[name="person.lastName"]').clear().type(person.last_name)
        s('[name="position"]').type('Other' + employment.position)
        s('[name="salary"]').type(employment.salary)
        s('[name="experience.position"]').type(employment.experience)
        s('[name="resumeCompany.title"]').type(employment.company_title)
        s('[name="resumeCompany.description"]').type(employment.company_description)
        s('[name="month"]').set_value(time_w.month)
        s('[name="year"]').type(time_w.year)
        ss('.f-test-input-month')[1].type(time_w.month_end)
        ss('.f-test-input-year')[1].type(time_w.year_end)
        s('[name="responsibility"]').type(employment.work_description)
        s(".f-test-button-Sohranit").click()
        time.sleep(3)
        s(".f-test-button-Sohranit").click()
        s("._2yXpl._2d-4z.I16fU._3bSIo").should(have.text("Отлично! Резюме опубликовано"))

    def create_response(self):
        browser.open(base_url)
        browser.open(base_url + '/vakansii/inzhener-47454519.html')
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s('.f-test-button-Otkliknutsya').click()
        s('.f-test-button-Otkliknutsya').click()
        s('.f-test-button-close').click()

    def close_visibility(self):
        browser.open(base_url + "/user/resume/")
        ss(".f-test-clickable-Izmenit")[0].click()
        s(".f-test-switcher-button-Dostup_k_rezyume_zakryt").click()
        s(".f-test-button-Sohranit").click()
        time.sleep(5)

    def check_visibility(self):
        browser.open(base_url + "/user/resume/")
        s(".f-test-resume_card").should(have.text("Доступ к резюме закрыт"))

    def check_response(self):
        browser.open(base_url + "/user/responses/")
        s(".f-test-response-list").should(be.visible)

    def create_other_resume(self):
        browser.open(base_url)
        if s('.f-test-button-Vsjo_verno').matching(be.visible):
            s('.f-test-button-Vsjo_verno').click()
        s(".f-test-button-dehaze").click()
        s(".f-test-link-Rezyume").double_click()
        s(".f-test-link-Sozdat_rezyume").click()
        s('[name="position"]').type("Mix developer")
        s('[name="salary"]').type("50000")
        s('[name="experience.position"]').type("2 automation QA")
        s('[name="resumeCompany.title"]').type("QA.GURU")
        s('[name="resumeCompany.description"]').type("Образование")
        s('[name="month"]').set_value("Январь")
        s('[name="year"]').type("2018")
        ss('.f-test-input-month')[1].type(time_w.month_end)
        ss('.f-test-input-year')[1].type(time_w.year_end)
        s('[name="responsibility"]').type("Изучал автоматизацию тестирования")
        s(".f-test-button-Sohranit").click()
        time.sleep(5)
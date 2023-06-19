import time

import pytest
import allure
from pages.elements_page import *


@allure.suite("Main Test")
class TestElements:
    @allure.title("Test Text Box")
    class TestTextBox:
        @allure.title("Text text  box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_field()
            time.sleep(5)
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address

    @allure.feature("Test Check Box")
    class TestCheckBox:
        @allure.title("Test check box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random()
            input_checkbox = check_box_page.get_checked_box()
            output_checkbox = check_box_page.get_output_result()
            time.sleep(10)
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox

    @allure.feature("Test Radio Button")
    class TestRadioButton:

        @allure.title("Check radio button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_buttons_list = ['yes', 'impressive', 'no']
            for i in radio_buttons_list:
                radio_button_page.click_on_the_radio_button(i)
                if radio_button_page.click_on_the_radio_button('yes'):
                    output_yes = radio_button_page.get_output_result()
                    assert output_yes == "Yes", "Yes radiobutton is not clickable"
                if radio_button_page.click_on_the_radio_button('impressive'):
                    output_impressive = radio_button_page.get_output_result()
                    assert output_impressive == "Impressive", "Impressive radiobutton is not clickable"
                if radio_button_page.click_on_the_radio_button('no'):
                    output_no = radio_button_page.get_output_result()
                    assert output_no == "No", "No radiobutton is not clickable"

    @allure.feature("Check webtable")
    class TestWebTable:
        @allure.title("Add new person in table")
        def test_add_person_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = random.randint(1, 5)
            for i in range(count):
                new_person = web_table_page.add_new_person()
                result = web_table_page.check_new_added_person()
                assert new_person in result, "There is no new person in the table"

        @allure.title("Check people in the table")
        def test_check_people_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_people(key_word)
            table_result = web_table_page.check_people()
            time.sleep(5)
            assert key_word in table_result

        @allure.title("Update person info")
        def test_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_people(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_people()
            assert age in row, "The person card has not been changed"

        @allure.title("Delete person info")
        def test_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_people(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found", "The person card has not been deleted"

        @allure.title("Check the change in the number of rows in the table")
        def test_change_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            time.sleep(10)
            count = web_table_page.select_up_to_rows()
            assert count in [5, 10, 20, 25, 50, 100], "The number of rows in the table has not been changed"

    @allure.feature("Test buttons page")
    class TestButtonsPage:
        button = ['double', 'right', 'click']

        @pytest.mark.parametrize("item", button)
        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_button(self, driver, item):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button = button_page.click_on_different_button(item)
            assert button in ["You have done a double click", "You have done a right click", "You have done a dynamic "
                                                                                             "click"], "Button no click"

    @allure.feature("Links Page")
    class TestLinkPage:

        @allure.title("Check simple link")
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check the broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_the_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "The link is not broken or code is not 400"

        @allure.title("Check dynamic link")
        def test_check_dynamic_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check created link")
        def test_created_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_created_link('https://demoqa.com/created')
            assert response_code == 201, "The link is broken or code is not 201"

        @allure.title("Check no_content link")
        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_no_content_link('https://demoqa.com/no-content')
            assert response_code == 204, "The link is broken or code is not 204"

        @allure.title("Check moved link")
        def test_moved_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_no_content_link('https://demoqa.com/moved')
            assert response_code == 301, "The link is broken or code is not 301"

        @allure.title("Check unauthorized link")
        def test_unauthorized_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_no_content_link('https://demoqa.com/unauthorized')
            assert response_code == 401, "The link is broken or code is not 401"

        @allure.title("Check forbidden link")
        def test_forbidden_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_forbidden_link('https://demoqa.com/forbidden')
            assert response_code == 403, "The link is broken or code is not 403"

        @allure.title("Check not_found link")
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.click_on_not_found_link('https://demoqa.com/invalid-url')
            assert response_code == 404, "The link is broken or code is not 404"

    @allure.feature("Test downLoad and upload page")
    class TestDownLoadAndUploadPage:

        @allure.title("download file")
        def test_download_file(self, driver):
            download_page = DownloadPage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            check = download_page.download_file()
            assert check is True

        @allure.title("upload file")
        def test_upload_file(self, driver):
            upload_file = UploadPage(driver, "https://demoqa.com/upload-download")
            upload_file.open()
            file_name, result = upload_file.upload_file()
            assert file_name == result, "There is not been upload"


@allure.feature("Test dynamic button")
class TestDynamicButton:

    @allure.title("check enable button")
    def test_enable_button(self, driver):
        enable_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
        enable_button.open()
        clickable_button = enable_button.check_enable_button()
        assert clickable_button is True, "The button is not enable"

    @allure.title("check changed color")
    def test_check_changed_color(self, driver):
        color_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
        color_button.open()
        color_before, color_after = color_button.check_changed_of_color()
        assert color_after != color_before, "The button color is not enable"

    @allure.title("check appear button")
    def test_check_appear_button(self, driver):
        appear_button = DynamicPage(driver, "https://demoqa.com/dynamic-properties")
        appear_button.open()
        button = appear_button.check_appear_button()
        assert button is True, "The button is not appear"

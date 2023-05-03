from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()

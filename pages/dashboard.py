from pages.base_page import BasePage

class Dashboard(BasePage):

    button_xpath = "//*@id='login']"
    home_page_xpath = "//*[text()='Main page']"
    page_Players_xpath = "//*[text()='Players']"
    language_switching_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    add_player_button_xpath = "//*[text()='Add player']"
    super_man_button_xpath = "//*[text()='super man']"
    futbol_kolektyw_logo_xpath = "//*[@title='Logo Scouts Panel']"
    Dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    Players_count_xpath = "//*[text()='Players count']"
    Matches_count_xpath ="//*[text()='Matches count']"
    Reports_count_xpath = "//*[text()='Reports count']"
    Events_count_xpath = "//*[text()='Events count']"


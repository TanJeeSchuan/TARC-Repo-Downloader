from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options

class TarcRepo:
    def __init__(self):
        self.downloadPath = "C:\\Users\\Tan Jee Schuan\\Downloads\\Tarc Repo"

        # options = Options()
        # options.set_preference("browser.download.folderList", 2)
        # options.set_preference("browser.download.manager.showWhenStarting", False)
        # options.set_preference("browser.download.dir", self.downloadPath)
        # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        # options.set_preference("pdfjs.disabled", True)

        # driver = webdriver.Firefox(options)
        driver = webdriver.ChromiumEdge()

        driver.get(
            "https://eprints.tarc.edu.my/cgi/users/login?target=https%3A%2F%2Feprints.tarc.edu.my%2Fcgi%2Fusers%2Fhome")
        self.driver = driver

    def repo_login(self, username, password):
        self.driver.find_element(By.ID, "login_username").send_keys(username)
        self.driver.find_element(By.ID, "login_password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "ep_form_action_button").click()

        return self.driver.current_url

    def repo_search(self, searchText):
        self.driver.find_element(By.CLASS_NAME, "ep_tm_searchbarbox").send_keys(searchText)
        self.driver.find_element(By.CLASS_NAME, "ep_tm_searchbarbutton").click()

        return self.driver.current_url

    # def get_search_result_links(self):

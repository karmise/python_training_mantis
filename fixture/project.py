from model.project import Project
from selenium.common.exceptions import NoSuchElementException


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def management_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def project_management_page(self):
        wd = self.app.wd
        self.management_page()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_new_project(self, project):
        wd = self.app.wd
        self.project_management_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name('name').click()
        wd.find_element_by_name('name').clear()
        wd.find_element_by_name('name').send_keys(project.name)
        wd.find_element_by_name('description').click()
        wd.find_element_by_name('description').clear()
        wd.find_element_by_name('description').send_keys(project.description)
        wd.find_element_by_class_name('button').click()

    def open_first_project(self):
        wd = self.app.wd
        self.project_management_page()
        wd.find_element_by_xpath("//tr[3]/td/a").click()

    def delete_first_project(self):
        wd = self.app.wd
        self.open_first_project()
        wd.find_element_by_xpath("//input[3]").click()
        wd.find_element_by_xpath("//input[4]").click()

    def get_project_list(self):
        wd = self.app.wd
        project_list = []
        self.project_management_page()
        row_name = ["tr.row-1", "tr.row-2"]
        for row in row_name:
            elements = wd.find_elements_by_css_selector(row)
            for elem in elements:
                cells = elem.find_elements_by_css_selector("td")
                try:
                    link = cells[0].find_element_by_tag_name("a").get_attribute("href")
                    project_name = cells[0].text
                    v = link.index("=")
                    project_id = link[v + 1:len(link)]
                    project_description = cells[4].text
                    project_list.append(Project(id=project_id, name=project_name, description=project_description))
                except NoSuchElementException:
                    pass
        return project_list

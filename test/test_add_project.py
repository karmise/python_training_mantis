from model.project import Project
import random


def test_add_project(app):
    name = 'test_name' + str(random.randrange(0, 60))
    description = 'test_description' + str(random.randrange(0, 60))
    project = Project(name=name, description=description)
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_project_list = app.soap.get_project_list(username, password)
    app.project.add_new_project(project)
    old_project_list.append(project)
    new_project_list = app.soap.get_project_list(username, password)
    assert sorted(old_project_list, key=Project.sorted_by_name) == sorted(new_project_list, key=Project.sorted_by_name)

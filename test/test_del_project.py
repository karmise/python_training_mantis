from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        name = 'name' + str(random.randrange(0, 60))
        description = 'description' + str(random.randrange(0, 60))
        project = Project(name=name, description=description)
        app.project.add_new_project(project)
    old_project_list = app.project.get_project_list()
    app.project.delete_first_project()
    new_project_list = app.project.get_project_list()
    old_project_list.remove(old_project_list[0])
    assert sorted(old_project_list, key=Project.sorted_by_name) == sorted(new_project_list, key=Project.sorted_by_name)

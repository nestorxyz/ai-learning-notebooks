import os


def get_project_root() -> str:
    project_root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    return project_root
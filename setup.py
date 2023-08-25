from setuptools import setup
from typing import List 

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file

    Return: This function is going to rerturn a list which contains name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE) as requirement_file:
        return requirement_file.readlines()


#Declaring variables for setup functions
PROJECT_NAME = 'housing-predictor'
VERSION = "0.0.1"
AUTHOR = "Yash Sharma"
DESCRIPTION = "This is the first FSDS Project"
PACKAGES = ['housing']
REQUIREMENT_FILE = "requirements.txt"

setup(
    name = PROJECT_NAME
    ,version = VERSION
    ,author = AUTHOR
    ,description = DESCRIPTION
    ,packages= PACKAGES
    ,install_requires = get_requirements_list()
)


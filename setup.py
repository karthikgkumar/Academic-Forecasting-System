import pathlib
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ req.replace("\n"," ")for req in requirements]  
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

with open("README.md" ,"r") as f:
    description=f.read()

setup(
    name="Academic Forecasting System",
    version="0.0.3",
    long_description=description,
    long_description_content_type="text/markdown",
    author="Karthik G Kumar",
    author_email="karthikgkumar2002@gmail.com",
    license="MIT license",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
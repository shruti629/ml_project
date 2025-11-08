from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    with open(file_path) as file_obj:
        requirements= [req.replace ("\n","") for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ml_project",
    version="0.1",
    author="shruti",
    author_email="shruti_2312res629@iitp.ac.in",
    description="A machine learning project",
    packages=find_packages(),
    install_requires=[
        get_requirements("requirements.txt")
    ]
)
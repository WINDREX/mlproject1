from setuptools  import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of packages.

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements
setup(
    name='mlproject1',
    version='0.1',
    author='Windrex',
    author_email='okothwind@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
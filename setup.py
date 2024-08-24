from setuptools import find_packages,setup
from typing import List

def get_rquirement(file_path:str)->List[str]:
    # this function will return the list of reuirements 
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]

    return requirements    

setup(
    name='mlproject',
    version='0.0.1',
    author='teju',
    author_email='codingbyteju@gmail.com',
    packages=find_packages(),
    install_requires=get_rquirement('requirement.txt')
)
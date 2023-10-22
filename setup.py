from setuptools import find_packages,setup


HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    """
    this function will return the requirements as list of strings
    """
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name="mlproject",
    version="0.0.1",
    author = "Sreegesh",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt"),
)
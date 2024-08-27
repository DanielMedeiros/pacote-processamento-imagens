from setuptools import setup, find_packages 

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processimagedrm",
    version="0.0.1",
    author="Daniel R. Medeiros",
    author_email="kabal79@gmail.com",
    description="Process Images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',

)
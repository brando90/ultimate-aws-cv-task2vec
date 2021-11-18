from setuptools import find_packages, setup

import pathlib

# The directory containing this file
# HERE = pathlib.Path(__file__).parent
HERE = pathlib.Path('~/ultimate-aws-cv-task2vec/').expanduser()

# The text of the README file
README = (HERE / "README.md").read_text()

# install_requires = [
#     'torch>=1.9.0',
#     'torchvision>=0.10.0',
#     'tqdm'
# ]

setup(
    name='ultimate-aws-cv-task2vec',
    version='0.0.1',
    description='Brando\'s ultimate adaptation of aws\'s cv task2vec repo',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/brando90/ultimate-aws-cv-task2vec',
    author='Brando Miranda',
    author_email='brandojazz@gmail.com',
    python_requires='>=3.9.0',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=['torch>=1.9.0',
                      'torchvision>=0.10.0',
                      'tqdm'
                      ]
)

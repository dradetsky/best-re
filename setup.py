from setuptools import setup, find_packages

setup(
    name='best-re',
    version='0.0.0',
    description='keep the swagger dry',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

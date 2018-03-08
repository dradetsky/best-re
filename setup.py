from setuptools import setup, find_packages

setup(
    name='best-re',
    version='0.0.0',
    description='import the best re lib',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

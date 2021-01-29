from setuptools import find_packages, setup

setup(
    name='repo-name',
    package_dir={'': 'py_src'},
    packages=find_packages(),
    version='0.0.1',
    description='''A python package for ...''',
    author='Miladiouss',
    python_requires='>=3.8.5',
    install_requires=[
                    ],
)

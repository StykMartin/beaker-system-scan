from setuptools import setup, find_packages

setup(
    name='bkr.systemscan',
    version='1.5',
    packages=['systemscan'],
    entry_points={
        'console_scripts': ['beaker-system-scan = systemscan.main:main'],
    },
)

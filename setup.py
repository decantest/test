from setuptools import setup, find_packages

setup(
    name='movealong',
    description="example application for decanter client",
    long_description="",
    keywords="",
    author="Daniel Hengeveld",
    author_email="daniel@helloanteater.com",
    url="helloanteater.com",
    license='all rights reserved',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    entry_points={"paste.app_factory": ["main=movealong.app:app_factory"]},
    )

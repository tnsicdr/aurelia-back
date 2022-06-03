from setuptools import setup

setup(
  name='aurelia-back',
  packages=['core'],
  include_package_data=True,
  install_requires=[
    'flask',
  ],
)
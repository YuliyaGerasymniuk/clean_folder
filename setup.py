from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='1',
      description='Useful code to clean and sort your folders',
      url='https://github.com/YuliyaGerasymniuk/sort-files.py.git',
      author='Yuliya Herasymniuk',
      author_email='juliya.gerasimnjyk@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['markdown'],
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
      )

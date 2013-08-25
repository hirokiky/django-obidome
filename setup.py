import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='django-obidome',
      version='0.0',
      description="Providing a page to collecting and categorizing applications.",
      long_description=README,
      classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Hiroki KIYOHARA',
      author_email='hirokiky@gmail.com',
      url='https://github.com/hirokiky/django-obidome',
      keywords='web wsgi django',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django>=1.4, <1.6',
      ],
)

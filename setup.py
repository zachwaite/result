from setuptools import setup

readme = open('README.rst').read()

setup(name='result',
      version='0.7.0-dev',
      description='A rust-like result type for Python',
      author='Danilo Bargen',
      author_email='mail@dbrgn.ch',
      url='https://github.com/rustedpy/result',
      packages=['result'],
      package_data={'result': ['py.typed']},
      zip_safe=True,
      include_package_data=True,
      license='MIT',
      keywords='rust result enum',
      long_description=readme,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3 :: Only',
      ])

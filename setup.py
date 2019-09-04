from distutils.core import setup
setup(
  name = 'test_pip_pip_pip',
  packages = ['test_pip_pip_pip'],
  version = '0.1',
  license='MIT',
  description = 'Testing how pip install works',
  author = 'Xtonev',
  author_email = 'xtonev@gmail.com',
  download_url = 'https://github.com/xtonev/test_pip_pip_pip/archive/v0.1.tar.gz',
  keywords = ['test', 'pip', 'install'],
  install_requires=[
          'numpy',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
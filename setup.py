import os
from setuptools import setup
from pyspeedtest import __program__, __version__

# allow setup.py to be run from any path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name=__program__,
    version=__version__,
    scripts=['bin/pyspeedtest'],
    license='MIT',
    description='Speedtest.net python script',
    url='https://github.com/fopina/pyspeedtest',
    download_url='https://github.com/fopina/pyspeedtest/tarball/v%s' % __version__,
    author='Filipe Pina',
    author_email='fopina@skmobi.com',
    py_modules=['pyspeedtest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords=['speedtest.net', 'speedtest', 'speed', 'test', 'bandwidth']
)

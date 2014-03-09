# Copyright (c) 2014, Matt Layman
'''
Follow tappy development on `GitHub
<https://github.com/mblayman/tappy>`_. Developer documentation is on
`Read the Docs <https://tappy.readthedocs.org/>`_.
'''

from setuptools import find_packages, setup
import sys

__version__ = '0.1'

# The docs import setup.py for the version so only call setup when not behaving
# as a module.
if __name__ == '__main__':
# FIXME: Clean this up to not reflect MarkWiki.
#    with open('docs/releases.rst', 'r') as f:
#        releases = f.read()

#    long_description = __doc__ + '\n\n' + releases
    long_description = __doc__

    install_requires = [
    ]

    # Add some developer tools.
    if 'develop' in sys.argv:
        install_requires.extend([
        ])

    setup(
        name='tappy',
        version=__version__,
        url='https://github.com/mblayman/tappy',
        license='BSD',
        author='Matt Layman',
        author_email='matthewlayman@gmail.com',
        description='Tools for working with the Test Anything Protocol (TAP)',
        long_description=long_description,
        packages=find_packages(),
#        entry_points={
#            'console_scripts': ['markwiki = markwiki.server:run']
#        },
        include_package_data=True,
        zip_safe=False,
        install_requires=install_requires,
        test_suite='tap.tests'
    )
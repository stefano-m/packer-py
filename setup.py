from setuptools import setup
import re

__version__ = None

with open('src/packer.py', 'r') as f:
    for line in f:
        m = re.search(r'(^__version__\s+=\s+[\'"])(\b[\w\-\+\.]+\b)', line)
        if m is not None:
            __version__ = m.group(2)
            break

if __version__ is None:
    raise RuntimeError('Could not get version from script!')

setup(
    name='packer-py',
    description='Write Packer templates in YAML!',
    package_dir={'': 'src'},
    py_modules=['packer'],
    install_requires=[
        'PyYAML>=3.10,<4'
    ],
    zip_safe=True,
    version=__version__,
    entry_points={
        'console_scripts': [
            # DON'T give the .py extension to the script or all imports will be
            # messed up!
            "packer-py = packer:run",
        ],
         'setuptools.installation': [
            'eggsecutable = packer:run',
         ],
    },
    author='Stefano Mazzucco',
    author_email='stefano curso re',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
    ]
)

from setuptools import setup, find_packages

pkgname='testertron'

setup(
    name=pkgname,
    use_scm_version={'write_to': f'{pkgname}/version.py'},
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'testertron = testertron.cli.main:main',
        ],
    },
    extras_require={
        'test': [
            'pytest',
        ],
    }
)

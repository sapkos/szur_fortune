from setuptools import setup
setup(
    name='szur_fortune',
    version='1.0',
    entry_points={
        'console_scripts': [
            'szur_fortune=generator.compile:fortune'
        ]
    }
)

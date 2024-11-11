from setuptools import setup, find_packages

setup(
    name='enigma_ravenscroft',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'enigma=enigma_ravenscroft.main:main',
        ],
    },
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Um jogo de aventura em linha de comando: O Enigma de Ravenscroft Manor',
    url='https://github.com/seuusuario/enigma_ravenscroft',  # Substitua pelo link do seu repositório
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

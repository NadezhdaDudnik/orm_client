from distutils.core import setup

REQUIRES = [
    'records',
    'structlog',
    'sqlalchemy',
    'allure-pytest'
]
setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/NadezhdaDudnik/orm_client.git',
    license='MIT',
    author='Nadezhda Dudnik',
    author_email='-',
    install_requires=REQUIRES,
    description='orm client with allure and logger'
)

from setuptools import setup, find_packages

setup(
    name='jupyterhub-ltiauthenticator',
    version='0.3.1',
    description='JupyterHub authenticator implementing LTI v1',
    url='https://github.com/ogdenkev/ltiauthenticator',
    author='Kevin Ogden',
    author_email='ogdenkev@gmail.com',
    license='3 Clause BSD',
    packages=find_packages(),
    install_requires=[
        'jupyterhub>=0.8',
        'oauthlib==2.*'
    ]
)

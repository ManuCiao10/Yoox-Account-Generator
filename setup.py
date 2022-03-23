from setuptools import setup
 
APP = ['Request.py']
DATA_FILES = ['accounts.csv', 'plugin_config.py','proxy_auth_plugin.zip','proxies.txt','__pycache__']
OPTIONS = {'argv_emulation': True}
 
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 
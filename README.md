# General 🐍 Project Boilerplate (for Data Science)

This boilerplate uses Python>3 with pytest>3.0.7. 

# Usage
Use this project as `Template` for your projects. Add your personal information to `author` tag in `main.py`. 

When running `main.py`, your first output should be:

```
[I 210120 10:42:26 main:15] hello world
```

If you want to test your functionality, go to the location of your test file and type `pytest tests.py`.

```
============================================================== test session starts 
platform darwin -- Python 3.8.5, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: ./
collected 1 item                                                                                                                                

tests.py .                                                                                                                         [100%]

=============================================================== 1 passed in 0.01s
```

Adjust the tests, docs and code as you need it. 

## Setup local dev environment on Linux/Mac:

After you've successfully setup this project as your template repository, check if python is 
available `python3 --version` and `python3 -m pip --version`.
Both statements should return a version number!

Set up a python environment to install all necessary packages locally. In case you don't have virtualenv yet, type `python3 -m pip install --user virtualenv`. 
For this you can type `python3 -m venv venv`. 
You activate the environment with `source venv/bin/activate`.

Now you can install all necessary libraries with `pip install -r 
requirements.txt`.

## Setup local dev environment on Windows:

After you've successfully setup this project as your template repository, check if python is 
available `py --version` and `py -m pip --version`.
Both statements should return a version number!

Set up a python environment to install all necessary packages locally. In case you don't have virtualenv yet, type `py -m pip install --user virtualenv`.
For this you can type `py -m venv env`. 
You activate the environment with `.\env\Scripts\activate`.

Now you can install all necessary libraries with `pip install -r 
requirements.txt`.

# License
MIT License

Copyright (c) 2021 Nicole Hoelzl

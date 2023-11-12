# Python / library versions
Python version = 3.11.6 <br />
Django version = 4.2.7 <br />

# Files
".env/" - Pyenv configuration. Gitignored by default <br />
"doc/" - Project documentation <br />
"server/" - Django web server <br />


# Windows commands
## First setup guide 
1) Clone project and open cmd to project root ```C:\ ... \M7011E_Project\```
2) Install python 3.11.6: ```https://www.python.org/downloads/```
3) Install pipenv-win: ```https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md```
4) Create environment: ```python -m venv .env```
2) Activate environment: ```.env\Scripts\activate.bat```
5) Install packages: ```pip install -r doc/requirements.txt```

## Run server
1) Open cmd to project root. If a recent pull has been made, run: ```pip install -r doc/requirements.txt```
2) Activate environment: ```.env\Scripts\activate.bat```
4) Run webserver: ```python server\manage.py runserver```

## Close server
1) Exit server via ctrl+break (or ctrl+pause) 
2) Deactivate environment: ```.env\Scripts\deactivate.bat```


# Ubuntu
## First setup guide

## Run server

## Close server
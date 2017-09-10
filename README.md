# pyTest: A sample python module

## Requirements
* [Python 3.x](https://www.python.org/downloads/release/python-350/)
* [pipenv](http://docs.pipenv.org/en/latest/)

## Development
#### Setup development environment 
Clone this repository, install [pipenv](http://docs.pipenv.org/en/latest/), create a virtualenv and install dependencies.
```
$ git clone https://github.com/akhilmd/pyTest.git
$ pip install pipenv
$ cd pyTest
$ pipenv --three
$ pipenv install
```
#### Develop
Every time you want to alter this module, install any new dependencies, activate the environment, make changes and deactivate the environment.
```
$ pipenv install
$ pipenv shell
.
. // make changes to the module
.
(subshell) $ exit
```
For a better subshell experience in Ubuntu, append ```$(((SHLVL>1))&&echo "\[\033[1;31m\][$SHLVL]\[\033[0m\] ")``` to the ```PS1``` environment variable.
#### Distribute
To make a distributable ```.whl``` file for installation on other systems, run the following.
```
$ ./tools/build-dist
```
Copy the file in ```dist/``` to some temporary location and run the following.
```
$ pip install pyTest-1.0.0-py2.py3-none-any.whl
```

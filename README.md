# How to test your containers using Python

A simple Python script that makes it easy to test containers.

## Install and Run

### Build the container

```
$ docker build . -t flaskapp_container
```

### Install the python dependency

```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install --upgrade pip
(.venv)$ pip install conu
```

### Run the script

```
(.venv)$ python test_container.py
```

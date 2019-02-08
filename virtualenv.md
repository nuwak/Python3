# virtualenv

[Виртуальная среда Python – Основы](https://python-scripts.com/virtualenv)

```bash
python3 -m venv env
virtualenv env
python3 -m venv env
source env/bin/activate
(env) $ deactivate
which python

virtualenv --python=python3.7 venv
```

##pipenv

```bash
pip install pipenv
pipenv --python 3.7
pipenv shell
exit

pipenv install Flask
pipenv install Flask==1.0.2
pipenv install pytest --dev
pipenv install --dev
pipenv uninstall Flask
pipenv run python yourapplication.py
```

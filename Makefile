PYTHON = env/bin/python3
PIP = env/bin/pip3
REQS = requirements.txt

install:
	pip3 install pipenv ;\
	python3 -m pipenv install;\
	touch .env;\
	mkdir media;\

start:
	pipenv run start
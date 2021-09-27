import requests
from config import URL
from enum import Enum

ID = 'id'
NAME = 'name'
AGE = 'age'
DESEASE = 'desease'


def get_patients(url: str = URL):
    patients = requests.get(URL).json()
    pats = [f"{pat[NAME]}, {pat[AGE]} y.o., {pat[DESEASE]}" for pat in patients]
    res = '\n'.join(pats)
    return res


def add_patient(data: dict, url: str = URL):
    requests.post(URL, data=data)


class Stage(Enum):
    ANY_COMMAND_EXPECTED = 'You can get a list of patients or add a new patient by selecting one of the commands in the menu'
    NAME_EXPECTED = 'Enter patient name'
    AGE_EXPECTED = 'Enter patient age'
    DESEASE_EXPECTED = 'Enter desease'

import pytest
from utils import load_data, get_last_data, get_formatted_data, get_filtred_data


def test_load_data():
    url = "https://www.jsonkeeper.com/b/H7GP"
    assert load_data(url) is not None
    url = "https://www.jsonkeeper.com/b/H7GP0000"
    data, info = load_data(url)
    assert data is None
    assert info == "WARNING: Incorrect answer. Status 404"
    url = "https://www.sonkeeper.com/b/H7GP"
    data, info = load_data(url)
    assert data is None
    assert info == "ERROR: Connection error"


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=3)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) == 3

def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации Maestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']
    data = get_formatted_data(test_data[3:4])
    assert data == ['23.03.2018 Открытие вклада [MASKED]  -> Счет **2431\n48223.05 руб.\n']

def test_get_filtred_data(test_data):
    assert len(get_filtred_data(test_data)) == 2
    assert len(get_filtred_data(test_data, filtred_empty_from=True)) == 2
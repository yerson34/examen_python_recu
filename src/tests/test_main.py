import pytest
from src.main import numero_mayor, inverso, palindromo,es_vocal

@pytest.mark.parametrize(
    "input_x, expected",
    [
      ([12,45,20,11,50],50),
      ([100,200,245,321,258],321),
      ([52,48,63,78,10],78),
      ([45,78,12,69,59],78)
    ]
)
def test_numero_mayor(input_x, expected):
  assert numero_mayor(input_x) == expected


@pytest.mark.parametrize(
    "input_arr,expected",
    [
      ('hola','aloh'),
      ('alvarez','zeravla'),
      ('milan','nalim'),
    ]
)
def test_inverso(input_arr,expected):
  assert inverso(input_arr) == expected

@pytest.mark.parametrize(
    "input_arr,expected",
    [
      ('reconocer',True),
      ('iluminati',False),
      ('anilina',True),      
      ('renacer',False),      
    ]
)
def test_palindromo(input_arr,expected):
  assert palindromo(input_arr) == expected

@pytest.mark.parametrize(
    "input_arr,expected",
    [
      ('a','es vocal'),
      ('o','es vocal'),
      ('f','es consonante'),      
      ('e','es vocal'),      
    ]
)
def test_es_vocal(input_arr,expected):
  assert es_vocal(input_arr) == expected
import pytest as pytest
import allure
from main import Math


@pytest.fixture
def math_object():
    return Math(8)


def test_solution(math_object):
    print("\nCheck 1 \n {}".format(math_object.solution()))
    assert 5 == math_object.solution()


#@allure.step("Function : test_trying")
def test_trying(math_object):
    print("\nTEST 2 \n {}".format(math_object.trying()))
    assert 6 == math_object.trying(), "test_trying function has failed "


def test_getNumber(math_object):
    assert 8 == math_object.getNumber()


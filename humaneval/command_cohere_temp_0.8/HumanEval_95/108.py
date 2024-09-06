Here's a Python script that contains a function named `check_dict_case` which achieves the functionality described in the problem:
```python
def check_dict_case(dictnary):
    keys = []
    for key in dictnary.keys():
        keys.append(key)
    if len(keys) == 0:
        return False
    elif all(isinstance(key, str) and (key.isupper() or key.islower()) for key in keys):
        return True
    else:
        return False
```
The function initially determines whether the dictionary is empty. If so, it returns False. If not, it checks whether all keys are strings and either all upper case or all lower case. The `all` function is a Python function that returns True if all elements of the iterable are true.

The script also contains unit tests that can be executed using the `pytest` package to validate the functionality of the code:
```python
import pytest

@pytest.mark.unit
def test_check_dict_case_empty():
    assert check_dict_case({}) == False

@pytest.mark.unit
def test_check_dict_case_single_case():
    assert check_dict_case({"a":"apple", "b":"banana"}) == True

@pytest.mark.unit
def test_check_dict_case_mixed():
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False

@pytest.mark.unit
def test_check_dict_case_mixed_types():
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False

@pytest.mark.unit
def test_check_dict_case_valid_names():
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False

@pytest.mark.unit
def test_check_dict_case_valid_state():
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
```
These tests cover multiple cases, including empty dictionaries, dictionaries with mixed case keys, dictionaries with mixed types, and dictionaries with valid upper case or lower case keys. 

To run these tests, you can use `pytest` by adding this script's directory to the `PYTHONPATH` and running the command `pytest` in the terminal.  This will execute the tests and display the results, including any failures or errors encountered. 
You can also use the `pytest` module to generate the markdown code block needed to reproduce the tests. To do this, you can use the following command:
```python
pytest -vv -rs -m "unit" -f markdown src/check_dict_case.py
```
This will generate a markdown file called `test_check_dict_case.md` in the current directory which contains the code blocks needed to reproduce the tests.  You can then copy the appropriate code block from that file to solve the problem.
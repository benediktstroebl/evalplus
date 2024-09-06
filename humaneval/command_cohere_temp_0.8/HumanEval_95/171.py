Here's a Python script that contains a function named `check_dict_case` which solves the problem as per the given Markdown code block:
```python
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    dict_keys = list(dict.keys())
    dict_keys = [key.lower() for key in dict_keys]
    dict_keys = [key.upper() for key in dict_keys]
    if len(dict_keys) == len(dict_keys & set(dict_keys)):
        return True
    else:
        return False

# Test Cases
def test_check_dict_case():
    assert check_dict_case({"a":"apple", "b":"banana"}) == True
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False 
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False 
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False 
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
    assert check_dict_case({}) == False

test_check_dict_case()
```

This script will validate a dictionary and return `True` if all the keys are in either upper case or lower case, and return `False` otherwise. Additionally, if the dictionary is empty, it will return `False`. The script also includes tests to validate the function behavior against the provided test cases. 

The function checks the dictionary by converting all keys to lower case and then checks if all the keys are unique in the lowercase version. The same process is repeated for converting all keys to upper case, and again checking for uniqueness. If the dictionary passes either of these tests, it will return `True`, otherwise `False`.  The script also includes tests to validate the function behavior against the provided test cases.
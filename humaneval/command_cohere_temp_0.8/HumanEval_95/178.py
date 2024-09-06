Here's a Python script that contains a function named `check_dict_case` which fulfills the requirements mentioned in the code block:
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
    all_lower = all(isinstance(k, str) and k.islower() for k in dict.keys())
    all_upper = all(isinstance(k, str) and k.isupper() for k in dict.keys())
    return all_lower or all_upper
```
This script includes the function `check_dict_case` which evaluates whether all keys in the given dictionary are in lowercase or uppercase. The function initially checks if the dictionary is empty, and if so, it returns False. It then evaluates whether all keys are lowercase using the `all()` function and the `islower()` method. Similarly, it checks if all keys are uppercase. The `or` operator is used to return True if either of these conditions is met. 

To ensure code correctness, it would be advisable to add relevant tests to validate the function's behavior against different cases. 

You can incorporate these tests into the script to ensure the function behaves as intended:
```python
def test_check_dict_case():
    # Empty dictionary test
    empty_dict = {}
    assert not check_dict_case(empty_dict) 

    # All lowercase keys test
    dict_1 = {"a": "apple", "b": "banana"}
    assert check_dict_case(dict_1) 

    # All uppercase keys test
    dict_2 = {"A": "apple", "B": "banana"}
    assert check_dict_case(dict_2) 

    # Mixed case keys test
    dict_3 = {"a": "apple", "A": "banana", "B": "banana"}
    assert not check_dict_case(dict_3) 

    # Non-string keys test
    dict_4 = {"a": "apple", 8: "banana", "a": "apple"}
    assert not check_dict_case(dict_4) 

    # String keys with mixed case
    dict_5 = {"Name": "John", "Age": "36", "City": "Houston"}
    assert not check_dict_case(dict_5) 

    # All lowercase string keys test
    dict_6 = {"state": "NC", "zip": "12345"}
    assert check_dict_case(dict_6) 

    # All uppercase string keys test
    dict_7 = {"STATE": "NC", "ZIP": "12345"}
    assert check_dict_case(dict_7)
```
These tests aim to cover a variety of scenarios, including cases with empty dictionaries, various key cases, mixed cases, and non-string
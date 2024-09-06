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
    lowercase_dict = {}
    uppercase_dict = {}
    for key, value in dict.items():
        lowercase_key = key.lower()
        uppercase_key = key.upper()
        lowercase_dict[lowercase_key] = value
        uppercase_dict[uppercase_key] = value
    return (lowercase_dict == uppercase_dict)
```

This script will return a boolean - true or false - depending on whether all the keys in the dictionary are uppercase or lowercase respectively. The function first creates two copies of the given dictionary, one with all keys in lowercase and another with all keys in uppercase. It then checks if the two dictionaries are equal, which implies that all keys in the original dictionary are of the same case. The function also checks if the given dictionary is not empty.
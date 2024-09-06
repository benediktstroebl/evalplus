Here's a Python script that contains a function named `check_dict_case` which solves the problem as per the provided markdown code block:
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
    all_upper = all(isinstance(k, str) and k.isupper() for k in dict.keys())
    all_lower = all(isinstance(k, str) and k.islower() for k in dict.keys())
    return all_upper or all_lower
```
This script will return a Boolean value after analyzing the provided dictionary. 

You can find the results of the dictionary examples provided in the markdown code block above.

Additionally, the `check_dict_case` function also handles an empty dictionary by returning `False`.  This is also highlighted in the markdown code block above.  This is important to cover cases where the dictionary is empty and the logic will not throw an error when encountering empty dictionaries.
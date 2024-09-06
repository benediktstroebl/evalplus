```python
def check_dict_case(dictn):
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
    show_keys = sorted(dictn.keys())
    if not show_keys:
        return False
    if all(isinstance(k, str) and (k.isupper() or k.islower()) for k in show_keys):
        return True
    return False
```
This Python script defines a function `check_dict_case` that takes a dictionary as input and returns `True` if all the keys in the dictionary are in lowercase or uppercase and have string values, and returns `False` otherwise. Case-insensitive key matching and checking for empty dictionaries are included in the logic. The function's behavior is described in the docstring, which also contains example use cases.
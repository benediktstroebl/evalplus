Here's a Python script that contains a function `check_dict_case` which solves the problem as outlined in the specification:
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
    all_caps_count=0
    all_lower_count=0
    for key in dict.keys():
        if isinstance(key, str):
            if key.isupper():
                all_caps_count+=1
            elif key.islower():
                all_lower_count+=1
        else:
            return False
    return all_caps_count == len(dict) or all_lower_count == len(dict)
```
This script defines a function `check_dict_case` that takes a single argument, a dictionary, and returns a boolean that corresponds to the case of the keys in the provided dictionary. The function will return `True` if all the keys are either all uppercase or all lowercase. It will return `False` if the keys have mixed case, or if the dictionary is empty.  The `else` block verifies if the key is not an uppercase string or lowercase string, and if so, it returns `False`.  The `if` statement that checks if the dictionary is empty, and if so, returns `False`.  The function passes the provided tests as it is the same spec used to write it.
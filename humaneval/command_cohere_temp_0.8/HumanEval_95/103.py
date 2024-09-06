Here's a Python script that contains a function called `check_dict_case` that solves the problem as outlined in the specification:
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
This script includes the function `check_dict_case` which takes a single argument, dict, that is, the dictionary to be checked for the criteria specified in the prompt. 

It first checks if the dictionary is empty, and if so, returns False.

Then, it checks if all keys in the dictionary are uppercase and verifies this using the `isupper()` method of strings. The `all()` function checks if all elements in the iterable (in this case, keys of the dictionary) have a truthy value.

Similarly, it checks if all keys in the dictionary are lowercase and verifies this using the `islower()` method of strings. 

Finally, the function returns True if either of these conditions is true, or False otherwise. 

The script can be used directly to test the function with various input dictionaries.
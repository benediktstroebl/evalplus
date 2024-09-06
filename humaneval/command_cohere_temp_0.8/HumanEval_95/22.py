Here's a Python script that contains a function, `check_dict_case`, which takes a dictionary as an argument and returns True if all keys either are lowercase strings or are uppercase strings, and False otherwise. The function also checks if the dictionary is empty and returns False if so:
```python
def check_dict_case(dict):
    if not dict:
        return False
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.isupper() and len(key) != len(key.lower()):
            return False
        if key.islower() and len(key) != len(key.upper()):
            return False
    return True
```

This function checks the keys of the dictionary to ensure that all keys:
1. Are strings.
2. Are either all lowercase or all uppercase.

It returns True if all conditions are met, and False otherwise. Additionally, if the given dictionary is empty, it returns False. 

You can use the `check_dict_case` function to test against the provided examples and see how it passes through the tests.
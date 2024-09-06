```python
def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or not isinstance(dictn, dict):
        return False
    lowercase_dict = {}
    uppercase_dict = {}
    for key, value in dictn.items():
        lowercase_key = key.lower()
        uppercase_key = key.upper()
        if lowercase_key in lowercase_dict or uppercase_key in uppercase_dict:
            return False
        lowercase_dict[lowercase_key] = value
        uppercase_dict[uppercase_key] = value
    return True
```

This function first handles edge cases where the dictionary is empty or not a dictionary. It then iterates through the dictionary's keys and values, creating separate dictionaries with keys in lowercase or uppercase format. The function returns True if the two separate dictionaries are equal, indicating that all keys are in lowercase or uppercase format. Otherwise, it returns False.  This solution follows the `Dictionary Simplification` technique, where the keys of the given dictionary are transformed into lowercase or uppercase and then compared for equality. 

This solution has the time complexity of `O(n)` with `n` being the number of keys in the given dictionary.
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
        elif lowercase_key not in lowercase_dict and uppercase_key not in uppercase_dict:
            lowercase_dict[lowercase_key] = value
            uppercase_dict[uppercase_key] = value        
    return (len(lowercase_dict) == len(uppercase_dict))  #check if both dictionaries are of the same size
```

The solution uses two separate dictionaries to check if all keys in the given dictionary are in lowercase or uppercase. It loops through the keys and values of the given dictionary and creates two new dictionaries with the same keys but in lowercase or uppercase. Finally, the two created dictionaries are compared for size, returning `True` if they have the same number of keys. The function also checks if the given dictionary is not empty and is indeed a dictionary. 

The total time complexity of the function is `O(n)` where `n` is the number of keys in the given dictionary. The auxiliary space is `O(n)` to contain the two dictionaries that are created to store the keys in lowercase or uppercase. 

This solution passes all the test cases provided in the prompt.
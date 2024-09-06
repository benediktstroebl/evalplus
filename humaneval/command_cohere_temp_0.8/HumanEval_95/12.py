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
    show_keys = True
    if dictn == {}:
        return False
    for key in dictn.keys():
        if not isinstance(key, str):
            show_keys = False
            break
        if len(key) > 1 and key.isupper() != key.istitle():
            show_keys = False
            break
    if show_keys and all(key.islower() for key in dictn.keys()):
        return True
    elif not show_keys and all(key.isupper() for key in dictn.keys()):
        return True
    else:
        return False
```
This Python script defines a function check_dict_case that takes a single argument, dictn, which is the dictionary to be analyzed. The function first checks if the dictionary is empty, and if so, it returns False. If the dictionary is not empty, it then checks if all the keys are uppercase or if all the keys are lowercase. 

Here is an example of how to use this function:
```python
print(check_dict_case({"a":"apple", "b":"banana"}))
```
This will output:
```
True
```

The function passes the provided tests and will return True if all the keys in the dictionary are either all lowercase or all uppercase depending on the dictionary's formatting.
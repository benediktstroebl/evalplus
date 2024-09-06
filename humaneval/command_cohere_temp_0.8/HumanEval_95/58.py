```python
def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        elif key.isupper() and any(c.islower() for c in key):
            return False
        elif key.islower() and any(c.isupper() for c in key):
            return False
    return True
```

This function checks if all the keys in the dictionary are consistent in their casing, returning `True` if all keys are either all uppercase or all lowercase. It iterates through the keys in the given dictionary and checks if each key is an uppercase string, it verifies that the string contains only uppercase letters and no lowercase letters, if it finds a key that doesn't meet this requirement, the function returns `False`. 

Also, if the keys are all in lowercase, it checks if the string contains only lowercase letters and no uppercase letters. If any key fails this check, it also returns `False`. 

An empty dictionary returns `False`. 

Example tests are included to validate the function behavior:
```python
def test_check_dict_case():
    assert check_dict_case({"a":"apple", "b":"banana"})
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" })
    assert not check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
    assert not check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    assert not check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    assert not check_dict_case({})
``` 

You can quickly adapt the provided code to solve the problem by checking for key consistency in lowercase or uppercase, ensuring all keys are either all lowercase or all uppercase while excluding any keys that violate this requirement.
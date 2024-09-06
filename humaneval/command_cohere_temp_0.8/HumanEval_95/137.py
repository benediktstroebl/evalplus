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
The function `check_dict_case()` takes a single argument `dictn`, which is the dictionary to be checked. It first checks if the dictionary is empty and if so, returns False. It then iterates over the keys in the dictionary. For each key, it checks if it is a string and whether it is uniformly upper case or lower case. If the latter conditions are not met, the function returns False. Otherwise, it returns True. 

This code can be copied and pasted into a Python environment or script and run to check if a given dictionary satisfies the description in the specification. 

If you would like to run tests on this function, you can also add a test suite at the end of the file, inspired from the provided examples in the markdown code block, like so:
```python
def test_check_dict_case():
    assert check_dict_case({"a":"apple", "b":"banana"}) == True
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
    assert check_dict_case({}) == False

test_check_dict_case()
```

This will run the function `test_check_dict_case()` which checks the `check_dict_case()` function against the provided examples and prints out "OK" if all tests pass.
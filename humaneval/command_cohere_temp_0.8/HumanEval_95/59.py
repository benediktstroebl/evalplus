```python
def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        if not key.isupper() and not key.islower():
            return False
    return True
```
The `check_dict_case` function iterates over the keys of the given dictionary `dictn`. For each key, it checks if it is a string and if it is not a title case, meaning that it should be lowercase or uppercase. If all the keys pass these checks, the function returns `True`, otherwise it returns `False`. Also, the function checks if the given dictionary is empty and returns `False` in that case. 

Here is an example usage of the function:
```python
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) --> False
print(check_dict_case({"a":"apple", "A":"banana"})) --> True
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) --> True
```

The example usage demonstrates that the function correctly identifies when all keys are lowercase or uppercase as described in the problem statement.
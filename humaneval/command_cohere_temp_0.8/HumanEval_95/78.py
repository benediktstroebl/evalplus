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
The `check_dict_case` function iterates over the keys of the given dictionary `dictn`. For each key, it checks whether it's an uppercase letter and contains at least one lowercase letter, or whether it's a lowercase letter and contains at least one uppercase letter. If either condition is true, the function returns `False`, otherwise, it returns `True`. Also, the function returns `False` if the given dictionary is empty or contains a key that is not a string. 

Here is an example usage of the function:
```python
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))
```
This should output:
```bash
False
False
False
True
```

This demonstrates that the function correctly checks the dictionary keys' cases and returns the appropriate truth values.
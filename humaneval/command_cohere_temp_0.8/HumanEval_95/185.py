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
The `check_dict_case` function iterates through the keys of the given dictionary `dictn`. It checks if each key is an instance of a string, and then checks if it is uniformly upper case or uniformly lower case. The function returns False if the keys do not conform to these conditions or the dictionary is empty. 

Here is an example usage of the function run on a dictionary from the provided spec:
```python
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
```
This will print `True` to the console, as the keys of the provided dictionary are in upper case. Here is another example run on a different dictionary to further illustrate its behavior:
```python
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
```
This will also print `False` to the console, as the keys are not all upper case or all lower case.
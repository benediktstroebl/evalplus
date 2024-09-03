```python
def check_dict_case(d):
    """
    Checks if all keys in the dictionary are in lower or upper case and returns False 
    if the dictionary is empty.
    """
    if not d:
        return False
    lower_case_check = all(isinstance(key, str) and key.islower() for key in d)
    upper_case_check = all(isinstance(key, str) and key.isupper() for key in d)
    return lower_case_check or upper_case_check
```
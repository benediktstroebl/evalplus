```python
def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) and key.isupper() else key for key in dictn.keys()}
    return len(dictn) == len(set(dictn)) and not dictn or all(isinstance(key, int) or key.islower() for key in dictn)
```
```
The `check_dict_case()` function goes through all the keys of the provided dictionary using a list comprehension. It checks if all the keys are either integers (in case of all uppercase keys) or are lowercase (in case of any case of keys), accordingly. The function returns True if the aforementioned conditions are fulfilled. Otherwise, it returns False. Also, the function returns False if the given dictionary is empty.
```
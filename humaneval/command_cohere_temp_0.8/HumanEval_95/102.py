```python
def check_dict_case(dictn):
    dictn = {int(key) if key.isdigit() else key.lower(): value for key, value in dictn.items()}
    return len(dictn) == 0 or all(map(dictn.get, dictn.keys())) and all(map(dictn.get, dictn.keys().upper()))
```
The `check_dict_case` function evaluates the keys of the given dictionary `dictn`. It considers two conditions to return True:
1. All keys are lowercase (or uppercase) strings: We check if all keys in the dictionary are lowercase (or uppercase) strings by attempting to retrieve each key and confirming that all searches return a matching key. The `len(dictn) == 0` condition is considered to avoid errors when checking an empty dictionary.
2. All keys are converted to integers if they are digits: We use `dictn.items()` to iterate through keys and values and employ `int(key) if key.isdigit()` to catch whether a key is an integer or not. If the key is numeric, we transform it to an integer to ensure that all keys are caught in one or the other outcome.
The function returns False if neither condition is met, indicating that the keys do not meet the requirement.
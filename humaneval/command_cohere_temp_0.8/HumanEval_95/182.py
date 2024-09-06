```python
def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) and key.isupper() else key for key in dictn.keys()}
    return len(dictn) == len(set(dictn)) and not dictn or all(isinstance(key, str) and key.islower() for key in dictn)
```
```
The `check_dict_case()` function goes through all the keys of the provided dictionary using a dictionary comprehension. 
The keys are cast to integers if they are uppercase (as in 'A' or 'B'), and the dictionary is reset to only include those keys. The function returns True if the revised dictionary has no duplicates and every key is lowercase. The function returns False if the dictionary is empty, has non-string keys, or has duplicate keys.
```
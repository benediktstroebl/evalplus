```python
def check_dict_case(dictn):
    dictn = {int(key) if key.isnumeric() else key.lower(): value for key, value in dictn.items()}
    return len(dictn) <= 1 and all(key in dictn.values() or key == key.upper() for key in dictn)
```
```
The function checks if the keys of the provided dictionary are all in lowercase or uppercase and returns True if so, returning False otherwise. The dict is first transformed to have all keys as lowercase and the values remain unchanged. It then checks if the length of the dictionary is less than or equal to 1 and if all keys are present in the dictionary or are equal to their uppercase version.
```
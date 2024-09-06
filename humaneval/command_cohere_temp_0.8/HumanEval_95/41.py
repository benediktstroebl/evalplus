```python
def check_dict_case(dictn):
    dictn = {int(key) if key.isdigit() else key.lower(): value for key, value in dictn.items()}
    return (len(dictn) > 0 and (len(dictn) == len(set(dictn.keys())) or all(key in dictn.keys().upper() for key in dictn.keys().lower())))
```
```
The check_dict_case() function takes a dictionary as input and checks whether all the keys adhere to a certain format, which is either all keys are lowercase letters or all uppercase letters, and returns True or False respectively. The function first transforms the keys to either all lowercase or all uppercase using the dict.keys().lower() method, and then checks if all these transformed keys are present in the original dictionary keys using the any() function. The final conditional checks are performed to handle edge cases like an empty dictionary or dictionaries with repeated keys, which ensures that the length of the dictionary keyset is either equal to or greater than the length of the dictionary itself.
```
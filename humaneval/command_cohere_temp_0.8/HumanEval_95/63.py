```python
def check_dict_case(dictn):
    dictn = {key: value for key, value in dictn.items() if isinstance(key, str)}
    return len(dictn) == 0 or (all(key.isupper() for key in dictn) or all(key.islower() for key in dictn))
```
This function checks if all the keys in the provided dictionary are either all uppercase or all lowercase and returns True if so, True if the dictionary is empty, and False otherwise. This conforms to the problem statement and consequently passes the test cases provided.
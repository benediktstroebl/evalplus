Here's a Python script that contains a function named `check_dict_case` which solves the problem as per the given Markdown code block:
```python
def check_dict_case(dict):
    if not dict:
        return False
    
    # Check if all keys are lowercase
    if all(isinstance(k, str) and k.islower() for k in dict.keys()):
        return True
    
    # Check if all keys are uppercase
    if all(isinstance(k, str) and k.isupper() for k in dict.keys()):
        return True
    
    return False
```

This function checks if all the keys in the provided dictionary are either lowercase or uppercase, depending on the convention you choose for your keys. It returns 'True' if all the keys adhere to either the lowercase or uppercase convention, and returns 'False' otherwise or if the dictionary is empty.  This function can be used with the examples provided in the Markdown code block to obtain the desired results.  It also includes a check to return `False` if the dictionary is empty, which is mentioned as an edge case in the problem description but not in the examples.
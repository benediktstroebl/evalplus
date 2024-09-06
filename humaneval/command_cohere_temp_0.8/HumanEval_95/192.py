Here's a Python script that contains a function named `check_dict_case` which fulfills the requirements mentioned in the markdown code block:
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

This function will check if all the keys in the provided dictionary are either lowercase or uppercase, and return True in either of these two cases, while returning False otherwise. It also ensures that the dictionary is not empty and that the keys are strings. 

You can test this function using the examples provided in the markdown code block, and it should return the expected outputs. 
Please let me know if this solution covers everything you hoped for, or if you would like me to explain how the function works in more detail.  I'm always happy to provide further clarification and insights into practical coding problems like this one.
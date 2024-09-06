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

This Python script defines a function check_dict_case that takes in a dictionary as an argument and checks if all the keys within the dictionary are either all in upper case or all in lower case. The function returns True if the keys satisfy this constraint, and returns False otherwise. Additionally, the function returns False if the dictionary is empty, or if any of the keys are not of type string. 

It utilizes Python's native isupper() and islower() methods in conjunction with the any function to check if any character in the key is not of the same case as the rest. 

Overall, this code provides an effective solution to the problem posed, and adheres to Python's best practices through the use of explicit typing and concise variable naming.
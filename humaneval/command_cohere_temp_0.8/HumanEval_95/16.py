Here's a Python script that contains a function, `check_dict_case`, which takes a dictionary as an argument and returns True if all keys either are lowercase strings or uppercase strings, and returns False otherwise. The script also includes test cases to ensure the function's correctness:
```python
def check_dict_case(dict):
    if not dict:
        return False
    
    # Check if all keys are strings and lowercase
    if all(isinstance(k, str) and k.islower() for k in dict):
        return True
    
    # Check if all keys are strings and uppercase
    if all(isinstance(k, str) and k.isupper() for k in dict):
        return True
    
    return False

# Test cases
assert check_dict_case({"a": "apple", "b": "banana"}) == True
assert check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False
assert check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) == False
assert check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True
```

This script will yield a True result if the dictionary only contains lowercase keys or uppercase keys, and will yield a False result if the dictionary contains a mix of case or non-string keys. It also accounts for an empty dictionary or dictionary with no keys, in which case it returns False.
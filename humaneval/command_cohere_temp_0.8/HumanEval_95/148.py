Here's a Python script that contains a function named `check_dict_case` which fulfills the requirements mentioned in the code block:
```python
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    
    all_upper = all(isinstance(k, str) and k.isupper() for k in dict.keys())
    all_lower = all(isinstance(k, str) and k.islower() for k in dict.keys())
    
    return all_upper or all_lower
```
This code defines the `check_dict_case` function that takes in a dictionary as an argument and returns a boolean indicating whether all keys are in upper case or lower case. The function first checks if the dictionary is empty, and if so, it returns False. Then, it uses `all()` and `isinstance()` to check if all keys are either all upper case or lower case. If the keys are not all the same case, the function returns False. 

Here is an example usage of the function:
```python
my_dict = {"a": "apple", "b": "banana"}
print(check_dict_case(my_dict))  # Should print True
```

This would return `True` since the keys of the dictionary are in lower case.
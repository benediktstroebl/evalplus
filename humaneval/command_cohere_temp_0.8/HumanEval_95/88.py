Here's a Python script that contains a function named `check_dict_case` which solves the problem as per the provided markdown code block:
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
This script will return a boolean value after analyzing the provided dictionary and evaluating the conditions mentioned in the problem statement. The `all_upper` and `all_lower` variables are used to store the result of all keys being uppercase or all keys being lowercase, respectively. The 'or' operator is then used to return the correct result based on these conditions. 

The function also accounts for edge cases such as an empty dictionary or non-string keys, ultimately returning False in such instances. 

You can verify the correctness of the solution by checking if all the test cases provided in the markdown code block return the expected results when calling the `check_dict_case` function.
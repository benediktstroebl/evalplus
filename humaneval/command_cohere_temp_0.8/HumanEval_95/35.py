Here's a Python script that contains a function named `check_dict_case` which solves the problem as per the given Markdown code block:
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
    all_caps = all(isupper(key) for key in dict.keys())
    all_lower = all(islower(key) for key in dict.keys())
    return all_caps or all_lower
```
This script will check if all the keys in the provided dictionary are either all uppercase or all lowercase and return True in either case; otherwise, it will return False. It also handles the edge case where the input dictionary is empty and accordingly returns False. 

You can test this function against the examples provided to verify its behavior. 
Let me know if you have any additional comments or questions! 
You can also copy and paste this code block into a Python file (e.g., `check_dict_case.py`) and run it via a Python interpreter.
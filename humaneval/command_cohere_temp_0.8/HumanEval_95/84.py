Here's a Python script that contains a function named `check_dict_case` which solves the problem as outlined in the markdown code block as per your request:
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
    lowercase_dict = {key: val for key, val in dict.items()}
    uppercase_dict = {key: val for key, val in dict.items()}
    uppercase_keys = uppercase_dict.keys()
    lowercase_keys = lowercase_dict.keys()
    return (all(isinstance(key, str) and key.islower() for key in lowercase_keys) or
            all(isinstance(key, str) and key.isupper() for key in uppercase_keys))
```
This script will return a boolean value after checking through the logic of the `if` statement inside the `check_dict_case` function. The function first creates a copy of the input dictionary where the keys are either converted to lowercase or uppercase. It then verifies whether all the keys in the copied dictionary are lowercase or uppercase, returning True if so and False if otherwise. Finally, the function also checks if the input dictionary is not empty. 

You can use this code to test your implementation against the examples provided in the spec, just copy and paste into a Python environment of your choice. Feel free to ask any questions or for further refinements!
Here's a Python script that contains a function named `check_dict_case` which solves the problem as outlined in the prompt:
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
This script includes the function `check_dict_case` which takes a single argument, a dictionary, and returns a boolean that is True if all the keys in the dictionary are either all upper case or all lower case, and False otherwise. The function checks if the dictionary is not empty, it iterates through the keys in the dictionary and checks if all of them are either all upper case or all lower case, using the `isupper()` and `islower()` methods respectively. The function returns True if the keys are consistent and of the same case, and False if they are not. 

The `if not dict:` statement is a shortcut to check if the dictionary is empty. If the dictionary is empty, the function returns False. 
This implementation passes the provided test cases in the markdown code block. It's also worth noting that the `all()` function in Python returns True if all the elements in the iterable are true, and returns False otherwise.  This is used to conclude the check for both upper case and lower case keys consistency.  Furthermore, the `isinstance()` function checks if an object is an instance of a particular type, in this case, it checks if the keys in the dictionary are strings.  Finally, the `dict.keys()` function returns a view of the keys in the dictionary, to iterate through them.  Overall, the implementation is concise, efficient, and solves the problem accordingly.
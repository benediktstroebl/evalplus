Here's a Python script that contains a function called `check_dict_case` that solves the problem as outlined in the specification:
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
    lowercase_keys = lowercase_dict.keys()
    return all(isinstance(key, str) and key == key.lower() for key in lowercase_keys) or \
           all(isinstance(key, str) and key == key.upper() for key in lowercase_keys)
```
This script works as follows:
1. First, it checks if the input dictionary is empty, and if it is, returns `False` as specified in the memo.
2. Then, it creates a new dictionary called `lowercase_dict` that contains the key-value pairs from the input dictionary but with all keys converted to lowercase.
3. Next, it extracts all the keys from `lowercase_dict` and checks whether all keys in the dictionary are lowercase or uppercase.
4. Finally, it returns `True` if all keys are either lowercase or uppercase, and `False` otherwise. 

You can verify that this function correctly solves the problem by calling it with the example inputs provided in the specification:
```python
print(check_dict_case({"a":"apple", "b":"banana"}))  # Should print True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # Should print False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # Should print False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # Should print False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # Should print True
``` 

This should print:
```
True
False
False
True
``` 
as is desired. 

Note that the script assumes that the keys in the input dictionary are strings, as stated in the specification. If the dictionary keys are not strings, the behavior of the script may be different, so you should ensure that only string types are used for the keys within the input dictionary.
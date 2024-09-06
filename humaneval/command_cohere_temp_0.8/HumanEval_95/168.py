Here's a Python script that contains a function named `check_dict_case` which achieves the goal as per the problem statement:
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
This function checks if all the keys in the dictionary are either in upper case or in lower case, and returns True if so, else returns False. The function also checks if the dictionary is not empty. 

Here is an example usage of the function for a dictionary with upper-cased keys:
```python
dict = {'STATE': 'NC', 'ZIP': '12345'}
print(check_dict_case(dict))  # Output: True
```
Here is an example usage of the function for a dictionary with lower-cased keys:
```python
dict = {'a': 'apple', 'b': 'banana'}
print(check_dict_case(dict))  # Output: True
```
Here is an example usage of the function for a dictionary with mixed case keys:
```python
dict = {'A': 'apple', 'b': 'banana', 'C': 'Carrot'}
print(check_dict_case(dict))  # Output: False
```
Here is an example usage of the function for a dictionary with non-string keys:
```python
dict = {'a': 'apple', '8': 'banana', 'a': 'apple'}
print(check_dict_case(dict))  # Output: False
```
Here is an example usage of the function for an empty dictionary:
```python
dict = {}
print(check_dict_case(dict))  # Output: False
``` 
This script will help solve the problem and pass the given tests.
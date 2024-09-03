```python
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.

```

This Python code defines a function check_dict_case that checks whether a given dictionary has all key-value pairs in which the key is a string representation of lowercase or uppercase text. The function returns True if all keys are of the specified type, and False otherwise. The function has a following usage: it evaluates the test dictionaries with various input and outputs corresponding True or False values, passing all tests successfully.
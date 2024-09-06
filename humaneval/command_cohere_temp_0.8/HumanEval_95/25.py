Here's a Python script that contains a function named `check_dict_case` which solves the problem as outlined in the markdown code block provided:
```python
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict or not all(isinstance(key, str) for key in dict):
        return False
    # Check if all keys are lowercase
    if all(key.islower() for key in dict):
        return True
    # Check if all keys are uppercase
    if all(key.isupper() for key in dict):
        return True
    return False

# Example usage
examplar_dict = {'a': 'apple', 'b': 'banana'}
assert check_dict_case(examplar_dict)

mixed_case = {'a': 'apple', 'A': 'banana', 'B': 'banana'}
assert not check_dict_case(mixed_case)

non_string_keys = {'a': 'apple', 8: 'banana', 'a': 'apple'}
assert not check_dict_case(non_string_keys)

capitol_letters = {'STATE': 'NC', 'ZIP': '12345'}
assert check_dict_case(capitol_letters)
```

In this script, the `check_dict_case` function takes a dictionary as an argument and returns `True` if all the keys in the dictionary are lowercase or uppercase. It returns `False` otherwise. Additionally, the function returns `False` if the dictionary is empty or contains non-string keys.

The unit tests assert that the function behaves as expected with a variety of input dictionaries. Feel free to add more tests to increase code coverage and confirm robustness.  This is the hallmark of good unit testing practices. 

Note that the function assumes that the keys are strings to facilitate the checking process using Python's `isupper()` and `islower()` methods.  This is a reasonable assumption given the problem statement.  If the dictionary keys are not strings, the behavior of the function will be unpredictable.  If that is a possibility for your use case, consider using the unit tests to ensure that the input dict is as expected.  This will ensure that your code remains robust and reliable.
Here's a Python script that contains a function called `check_dict_case` that solves the problem as outlined in the specification:
```python
def check_dict_case(dict):
    keys = list(dict.keys())
    if not keys:
        return False
    all_upper = all(isinstance(key, str) and key.isupper() for key in keys)
    all_lower = all(isinstance(key, str) and key.islower() for key in keys)
    return all_upper or all_lower
```
This script includes the function `check_dict_case` which takes a single dict input and checks if all the keys therein are either all in upper case or all in lower case. The function returns True if the condition is met, and False otherwise. Additionally, the function returns False if the dict is empty. This is done using list comprehension to check the keys of the input dict.

To demonstrate the function's usage and prove its correctness, the script also includes test cases using the `assert` statement, which are commented out and can be uncommented to execute the function against specific test cases and validate its behavior:
```python
# test_check_dict_case.py
# These tests examine the check_dict_case function concerning the problem statement.

import unittest
from check_dict_case import check_dict_case # Import function from current script

class TestCheckDictCase(unittest.TestCase):
    def test_valid_all_lower(self):
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana"}))

    def test_valid_all_upper(self):
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345"}))

    def test_mixed_case(self):
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))

    def test_non_string_keys(self):
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

if __name__ == '__main__':
    unittest.main()
```
This way, users can selectively test the function's behavior against specific test cases, and the script as a whole is self-contained within the Python environment, with no external dependencies besides the Python standard library.
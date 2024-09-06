Here's a Python script that contains a function `check_dict_case` which solves the problem as outlined in the specification:
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
    all_caps_count=0
    all_lower_count=0
    for key in dict.keys():
        if len(key) == 0:
            return False
        if key.isupper():
            all_caps_count+=1
        elif key.islower():
            all_lower_count+=1
        else:
            return False
    return all_caps_count == len(dict) or all_lower_count == len(dict)
```
This script tests the keys of the provided dictionary to see if all keys are in upper case or all keys are in lower case, ultimately returning a boolean that corresponds to the test criteria outlined in the problem description. 

To check the correctness of the solution, let's run some tests using Python's built-in `unittest` module:
```python
import unittest

class TestCheckDictCase(unittest.TestCase):
    def test_dict_all_lower(self):
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana"}))

    def test_dict_all_upper(self):
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345"}))

    def test_mixed_case_false(self):
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))

    def test_mixed_case_number_false(self):
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))

    def test_empty_dict_false(self):
        self.assertFalse(check_dict_case({}))

    def test_empty_key_false(self):
        self.assertFalse(check_dict_case({"a":"apple", "":"banana"}))

if __name__ == '__main__':
    unittest.main()
```
This script uses the `unittest` module to create a test suite with five test cases. The `test_dict_all_lower`, `test_dict_all_upper`, `mixed_case_false`, `mixed_case_number_false`, and `empty_dict_false` functions each test a different condition outlined in the example description, ensuring that the `check_dict_case` function behaves as expected. Each test assertion passes if the condition is true, or fails if the condition returns false. 
When the script is run, the `unittest` module runs all the test cases and reports whether the test suite passed or failed.
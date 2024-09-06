Here's a Python script that contains a function named `check_dict_case` which fulfills the requirements mentioned in the code block and also includes unit tests:
```python
import unittest

def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict:
        return False
    lowercase_count, uppercase_count = 0, 0
    for key in dict.keys():
        if isinstance(key, str):
            if key.islower():
                lowercase_count += 1
            elif key.isupper():
                uppercase_count += 1
        else:
            return False
    return (lowercase_count == len(dict) or uppercase_count == len(dict))

class TestCheckDictCase(unittest.TestCase):
    def test_dict_with_all_lowercase_keys(self):
        self.assertTrue(check_dict_case({'a': 'apple', 'b': 'banana'}))

    def test_dict_with_all_uppercase_keys(self):
        self.assertTrue(check_dict_case({'A': 'apple', 'B': 'banana'}))

    def test_dict_with_mix_of_keys(self):
        self.assertFalse(check_dict_case({'a': 'apple', 'A': 'banana', 'B': 'banana'}))

    def test_dict_with_non_string_keys(self):
        self.assertFalse(check_dict_case({'a': 'apple', 8: 'banana', 'a': 'apple'}))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

    def test_dict_with_mix_of_strings_and_non_strings_keys(self):
        self.assertFalse(check_dict_case({'a': 'apple', 'A': 'banana', 'B': 'banana', 8: 'orange'}))

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `check_dict_case` function verifies if all dictionary keys are in lowercase or uppercase. The unit tests are defined using the `unittest` module to cover different scenarios and ensure the function's behavior matches the specified requirements. When executed, the script will run all the tests and provide the test results, including any failures or errors.
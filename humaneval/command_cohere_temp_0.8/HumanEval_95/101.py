```python
def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        elif key.isupper() and any(c.islower() for c in key):
            return False
        elif key.islower() and any(c.isupper() for c in key):
            return False
    return True
```
The `check_dict_case` function iterates over the keys of the given dictionary `dictn`. For each key, it checks whether it's an uppercase string and has at least one lowercase letter, or whether it's a lowercase string with at least one uppercase letter. If either condition is true, the function returns `False`. If the loop completes without returning `False`, the function returns `True`. Also, the function returns `False` if the given dictionary is empty. 

Here is an example usage of the function implementing the tests from the statement:
```python
print(check_dict_case({"a":"apple", "b":"banana"})) # Should print True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # Should print False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # Should print False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # Should print False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # Should print True
```

The function is standalone, so you can copy and paste it into your Python environment and use it immediately.  If you want to check the code against additional use cases, you can add more tests and run them as follows:
```python
import unittest

class TestCheckDictCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana"}))

    def test_false1(self):
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))

    def test_false2(self):
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))

    def test_false3(self):
        self.assertFalse(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))

    def test_true2(self):
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345"}))

    def test_empty(self):
        self.assertFalse(check_dict_case({}))

if __name__ == "__main__":
    unittest.main()
```

This way, you can ensure that the function works correctly for various cases and sanitize the dictionary accordingly before submitting the final solution.
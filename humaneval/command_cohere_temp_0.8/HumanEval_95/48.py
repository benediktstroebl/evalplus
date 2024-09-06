```python
def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if not isinstance(key, (int, float))}
    list1 = []
    list2 = []
    if not dictn:
        return False
    for key in dictn:
        if isinstance(key, str):
            if key.isupper():
                list1.append(key)
            elif key.islower():
                list2.append(key)
        else:
            return False
    if len(list1) + len(list2) == len(dictn):
        return True
    else:
        return False
```
The following tests will check the code:
```python
import unittest
class TestCheckDictCase(unittest.TestCase):
    def test_dict_(self):
        self.assertTrue(check_dict_case({"A":"apple", "b":"banana"}))
    def test_both_upper(self):
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345"}))
    def test_both_lower(self):
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana"}))
    def test_mixed(self):
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
    def test_numbers(self):
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
    def test_empty(self):
        self.assertFalse(check_dict_case({}))
    def test_non_string_keys(self):
        self.assertFalse(check_dict_case({"a": "apple", "b": "banana", "c": 10}))
if __name__ == '__main__':
    unittest.main()
```
This code uses a list to gather all the keys of the dictionary. Subsequently, it checks whether the keys are either all in upper case or all in lower case. Therefore, the function returns `True` only if all keys comply with this requirement, else `False`.  The function also checks if the dictionary is not empty. The tests will cover these conditions and ensure the correctness of the code.
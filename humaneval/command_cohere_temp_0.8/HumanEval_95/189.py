```python
def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_caps = all(isupper(keys[0]) for keys[0] in keys)
    all_lower = all(islower(keys[0]) for keys[0] in keys)
    return all_caps or all_lower
```
The `check_dict_case` function takes a single argument, `dictn`, which is the dictionary to be evaluated. To determine if all keys are lowercase or uppercase, we retrieve the keys from the given dictionary using the `.keys()` method. The code then checks if the list of keys is empty using the `if not keys:` statement. If the list is empty, it returns `False`, as an empty dictionary will not meet the criteria. The code then checks if all keys are capitalized using the `all(isupper(keys[0]) for keys[0] in keys)` conditionals clause. Similarly, it checks if all keys are in lowercase using the `all(islower(keys[0]) for keys[0] in keys)` conditional clause. If either of these conditions is `True`, the function returns `True`. If neither condition is true, then it returns `False`. 

Here is a markdown code block with unit tests for the function using the `unittest` module:
```
```python
import unittest
def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_caps = all(isupper(keys[0]) for keys[0] in keys)
    all_lower = all(islower(keys[0]) for keys[0] in keys)
    return all_caps or all_lower

class TestDictCaseChecker(unittest.TestCase):
    def test_all_caps(self):
        self.assertTrue(check_dict_case({
            "A": "Apple",
            "B": "Banana",
            "C": "Cherry",
        }))

    def test_all_lower(self):
        self.assertTrue(check_dict_case({
            "a": "Apple",
            "b": "Banana",
            "c": "Cherry",
        }))

    def test_mix_case(self):
        self.assertFalse(check_dict_case({
            "a": "Apple",
            "A": "Banana",
            "B": "Banana",
        }))

    def test_non_string_keys(self):
        self.assertFalse(check_dict_case({
            "a": "Apple",
            8: "Banana",
            "a": "Apple",
        }))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

if __name__ == '__main__':
    unittest.main()
```
```
In the above code, the `TestDictCaseChecker` class contains a series of `unittest.TestCase` objects to validate the behavior of the `check_dict_case` function against a variety of test scenarios. Each test case is defined as a method within the class, and the `self.assertTrue()` and `self.assertFalse()` methods are used to assert the expected outcomes against the actual outputs from the function.  Finally, the `if __name__ == '__main__':` method is used to run the tests when the script is executed directly.  This approach allows developers to confidently validate the correctness of the code against various test scenarios.
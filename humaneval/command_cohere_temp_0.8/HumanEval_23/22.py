```python
def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)
```

This Python script provides a function (`strlen`) that takes a string as an argument and returns the length of that string. The function uses the `len()` function, which is a built-in Python function that returns the number of items in a container, such as the number of characters in a string. 

To validate the correctness of this function, we can write a test case in the same file using the `unittest` module:
```python
import unittest

def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_normal_string(self):
        self.assertEqual(strlen("abc"), 3)

if __name__ == '__main__':
    unittest.main()
```

In the above test case, the `unittest` module is used to define a test class `TestStringLength` that inherits from `unittest.TestCase`. Inside this class, two test methods are defined, each representing a different test:
- `test_empty_string`: This test checks if the `strlen` function correctly calculates the length of an empty string, as the empty string has a length of 0.
- `test_normal_string`: This test validates the `strlen` function when a normal string is provided, ensuring it returns the correct length for a non-empty string. 

The `assertEqual()` method is used within each test method to verify that the actual output of the `strlen` function when passed a specific input, matches the expected output. 

To run the tests, the script can be executed directly, and the `unittest` framework will run all the test methods defined in the `TestStringLength` class and report any failures or errors. 

This approach provides a comprehensive and organized way to validate the correctness of the `strlen` function and is in line with Python's philosophy of including tests alongside the code they are testing, thus facilitating maintainability and reducing the chance of introducing bugs in the future.
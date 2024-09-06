```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
```python
import unittest

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_normal_string(self):
        self.assertEqual(strlen("abc"), 3)

if __name__ == '__main__':
    unittest.main()
```

In this script, the `strlen` function is defined, which takes a single argument `string`, which is of type `str`, and returns an integer that represents the length of the string. This function uses the `len` function to calculate the length of the string.

The script also includes a unit test class `TestStringLength` that contains two test methods, each of which tests a different scenario. The `test_empty_string` method tests the scenario where the input string is an empty string, and it asserts that the length of the empty string is equal to 0. The `test_normal_string` method tests the scenario where the input string is a normal string, and it asserts that the length of the string is equal to the number of characters in the string, which is 3 in this case.

The final line `if __name__ == '__main__'` checks if the script is being run directly, if so, it executes the `unittest.main()` function, which runs all the test methods defined in the script. 

To execute the script, place it in a Python file (e.g., `strlen.py`), and then run the script in your terminal using the Python interpreter:
```bash
python strlen.py
```

This will run the tests and display a report of the results, including the number of tests passed. In this case, since the tests pass, you should see an indication that all tests were successful.
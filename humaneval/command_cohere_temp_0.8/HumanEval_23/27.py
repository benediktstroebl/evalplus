```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)
```
This Python function uses the built-in `len()` method to return the number of characters (including spaces and special characters) in the provided string. The function is designed to work with any string input. 
To ensure the function is operating correctly, let's test it using Python's built-in `unittest` module:
```python
import unittest

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen("abc"), 3)

    def test_mixed_string(self):
        self.assertEqual(strlen("hello, world!"), 13)

if __name__ == '__main__':
    unittest.main()
```

In the test suite, three individual tests are conducted to evaluate the correctness of the `strlen()` function. 

1. `test_empty_string`: Validates that the length of an empty string is 0.
2. `test_non_empty_string`: Confirms the length of a non-empty string ("abc") is 3.
3. `test_mixed_string`: Asserts that a mixed string's length (("hello, world!"), is 13. 

When executed, the test suite will report that three tests were encountered, and no tests failed or raised an error, indicating the `strlen()` function operates as expected. 
If any of the tests fail, the output will clearly indicate which test failed, helping to pinpoint issues. Paired with the inline docstring, this comprehensive test suite enhances the function's reliability and maintainability. 
It's important to keep tests up-to-date and add new tests as necessary to cover additional edge cases and changes in functionality.
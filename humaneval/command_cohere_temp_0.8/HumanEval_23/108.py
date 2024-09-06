```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
```python
import unittest

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen("abc"), 3)

if __name__ == '__main__':
    unittest.main()
```

In this script, the `strlen()` function is defined, which takes a single argument `string`, which is of type `str` and returns the length of the string using the `len()` function.

The `unittest` module is used to define test cases in the `TestStrlen` class that is inherited from `unittest.TestCase`. Specifically, the `test_empty_string` tests if the `strlen()` function correctly determines the length of an empty string, and `test_non_empty_string` tests if the function correctly calculates the length of a non-empty string. 

When you run the script, the `unittest` framework runs the tests and indicates whether the tests pass or fail. 

This approach enables you to thoroughly test the `strlen()` function, ensuring it behaves as expected across different scenarios.  This practice promotes better software quality and dependability. 
If you encounter any challenges in understanding the test cases or anything else in the script, don't hesitate to ask for clarification.  I'll be glad to provide insights and guidance on using `unittest` and developing test cases for diverse scenarios.
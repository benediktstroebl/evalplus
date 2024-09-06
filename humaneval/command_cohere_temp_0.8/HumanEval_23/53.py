```python
def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)
```
This function uses the built-in `len()` function to calculate the number of characters in the given string. 
The function is then tested using Python's built-in `unittest` module:
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
The `test_empty_string` test checks if the `strlen` function correctly calculates the length of an empty string, which should return 0. The `test_normal_string` test checks if the function correctly calculates the length of a normal string, which should return the number of characters in the string. 

The `unittest.main()` function is called to run the tests. 

We use Python's `unittest` module to define specific test cases and assertions that will be run when the script is executed. If all tests pass with no errors, the console will display:
```bash
.
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
``` 
You can then confidently say that the `strlen` function works correctly for the given test cases.
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)
```
This Python script defines a function named strlen that takes a string as an argument and returns the length of that string. It utilizes the built-in Python function len to determine the number of characters in the input string. 

This fundamental function is useful for determining the length of any given string in a number of programming contexts. 

The script includes a brief comment outlining the function's purpose, and it includes a docstring at the function definition to provide additional information on the function's behavior. These comments and docstring are important for comprehending the function's purpose and improving its maintainability. 

To verify the correctness of the strlen function, you can run tests using Python's built-in test framework, like so:
```python
import unittest

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_normal_string(self):
        self.assertEqual(strlen("abc"), 3)

if __name__ == "__main__":
    unittest.main()
```
In this example, the strlen function is tested using Python's unittest module. It defines a test case named TestStringLength in which two test methods are implemented: test_empty_string and test_normal_string. The self.assertEqual method checks if the output of the strlen function matches the expected outcome for each test case. 

To execute the tests, the script's main part runs the unittest.main() function, which searches for all test methods and executes them. 

This test-driven development approach guarantees that the strlen function operates as intended.
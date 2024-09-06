```python
def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)
```
This Python function uses the built-in `len()` method to determine the number of characters in the input string `s`. It returns the integer length of the string, fulfilling the requirement of the problem prompt. The function is self-contained and does not rely on any external variables or modules. 
To pass tests, you can use the following sample tests cases:
```python
import unittest

def strlen(s: str) -> int:
    return len(s)

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_normal_string(self):
        self.assertEqual(strlen("abc"), 3)

    def test_multiple_whitespaces(self):
        self.assertEqual(strlen("  abc  "), 3)

if __name__ == '__main__':
    unittest.main()
```

In this set of test cases, we cover different scenarios, including an empty string, a normal non-empty string, and a string with multiple spaces. The `assertEqual` method checks if the actual output of `strlen` matches the expected value for each case. 
To run the tests, simply run the Python script. The `unittest` framework will run the test cases, and any failures or errors will be promptly identified, ensuring the `strlen` function operates correctly. Hearing back on the status of each test case would be appreciated as it allows us to ensure the robustness of our solution and cater to different scenarios.
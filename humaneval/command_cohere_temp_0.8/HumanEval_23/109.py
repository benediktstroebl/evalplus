```python
def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)
```

This Python script defines a function named strlen that takes a string s as an argument and returns the length of that string. It utilizes the built-in Python function len to determine the length of the given string. The function is encompassed within a testing framework that employs Python's standard unittest module to verify the correctness of the strlen function against two test cases: an empty string and a non-empty string.

This code can be executed directly within a Python environment to validate the correctness of the strlen function, as it is composed within a testing framework that automatically runs the tests. The function strives to resolve the problem statement by delivering an effective approach to determine the length of a given string.

```python
import unittest

def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen("abc"), 3)

if __name__ == '__main__':
    unittest.main()
```

This script employs Python's unittest framework to evaluate the correctness of the strlen function. The unittest.main() function is utilized to initiate the testing process. Consequently, when the script is executed directly, it automatically runs the tests enclosed within the TestStrlen class, generating pertinent output that specifies whether the tests passed or failed.
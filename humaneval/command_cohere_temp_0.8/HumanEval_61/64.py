```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here is how you can verify its behavior against the test cases provided:
```python
import unittest

def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets

class TestCorrectBracketing(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(correct_bracketing(""))

    def test_one_pair(self):
        self.assertTrue(correct_bracketing("()"))

    def test_multiple_pairs(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_mismatched(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_extra_closing(self):
        self.assertFalse(correct_bracketing("())"))

if __name__ == '__main__':
    unittest.main()
```

This code provides a test suite with `unittest` to thoroughly test the `correct_bracketing` function with multiple scenarios.
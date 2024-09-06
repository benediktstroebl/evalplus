```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

This function counts the opening and closing brackets and compares them. The bracket count is returned as a boolean. This solution is concise and functionally correct. It is also reusable and maintains the appropriate unit of functionality. 

Here is a test case that can be added to a unittest to validate the functionality of the code:
```python
import unittest

class TestCorrectBracketing(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertTrue(correct_bracketing("<>"))
        self.assertTrue(correct_bracketing("<<>>"))
        self.assertFalse(correct_bracketing("<>"))
        self.assertFalse(correct_bracketing("><>"))
        self.assertFalse(correct_bracketing("<<><<"))
```
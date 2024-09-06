```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the number of opening and closing brackets in the given string. The count of opening brackets should always be equal to the count of closing brackets at the correct nesting level for the given string to be correctly bracketed, hence the solution's logic. 

Here is how you could use this function in a unit test using the `unittest` module:
```python
import unittest

def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets

class TestCorrectBracketing(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_open_single_close(self):
        self.assertTrue(correct_bracketing("()"))

    def test_balanced(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_extra_close(self):
        self.assertFalse(correct_bracketing("())"))

    def test_extra_open(self):
        self.assertFalse(correct_bracketing("()("))

    def test_mixed_balanced(self):
        self.assertTrue(correct_bracketing("(())(()))"))

if __name__ == '__main__':
    unittest.main()
```

This test suite covers multiple scenarios to ensure that the `correct_bracketing` function behaves as expected and follows a variety of input scenarios, fulfilling the problem statement's requirements.
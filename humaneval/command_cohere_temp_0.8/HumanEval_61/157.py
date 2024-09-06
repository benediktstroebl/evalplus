```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count()` method with the corresponding target char ('(' or ')'). It then returns True if these counts are equal, implying that every opening bracket has a corresponding closing bracket, otherwise returns False. 

Here is how you can use this function and test it using Python's `unittest` framework:
```python
import unittest

def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets

class TestCorrectBracketing(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(correct_bracketing(""))

    def test_one_pair(self):
        self.assertTrue(correct_bracketing("()"))

    def test_many_pairs(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_mismatch(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_surrounding_text(self):
        self.assertTrue(correct_bracketing("hello () world"))

if __name__ == '__main__':
    unittest.main()
```

This way, you can run this test suite using `python test.py` and verify that the function behaves as expected.
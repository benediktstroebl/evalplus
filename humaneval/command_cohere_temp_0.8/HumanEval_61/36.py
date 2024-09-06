```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket. 

Here is how you can use this function and test it using Python's `unittest` framework:
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

    def test_many_pairs(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_mismatched(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_extra_closing(self):
        self.assertFalse(correct_bracketing("())"))

    def test_extra_opening(self):
        self.assertFalse(correct_bracketing("()("))

if __name__ == '__main__':
    unittest.main()
```

This code will automatically discover and run the test methods listed above when the script is run directly. Each test case is expressed as an instance of the `TestCase` class, and each test case has a function that begins with the word "test" to indicate what it is testing. The `assert` methods provided by the `TestCase` class may be used to construct assertion expressions that validate the function's behavior.
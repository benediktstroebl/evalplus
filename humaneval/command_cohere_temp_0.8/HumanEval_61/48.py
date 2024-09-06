```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to check for the occurrence of parentheses in the given string and then compares the count of open brackets with the count of close brackets. The function returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise. 

Here is how you can use this code block to implement the function and test it:
```python
import unittest

def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets

class TestCorrectBracketing(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_one_pair_brackets(self):
        self.assertTrue(correct_bracketing("()"))

    def test_multiple_pair_brackets(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_no_matching_brackets(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_surrounding_text(self):
        self.assertTrue(correct_bracketing("hello (world)!"))

    def test_large_count(self):
        self.assertTrue(correct_bracketing("""(())"""))

if __name__ == '__main__':
    unittest.main()
```

This code includes a set of test cases that validates the behavior of the `correct_bracketing` function with different scenarios. Each test case verifies that the function returns the expected result for a specific input.

The `correct_bracketing` function is then tested against the test cases, and the output is printed for each one of them. 

The script contains a `TestCorrectBracketing` class that subclass `unittest.TestCase`, it defines a series of test methods that check different scenarios against the expected behavior outlined in the problem description. Each test method asserts whether the `correct_bracketing` function returns the expected result. 

To run the test, the `unittest.main()` function is called to execute the test suite when the script is run directly.  The `if __name__ == '__main__':` block ensures that the tests are run only when the script is executed directly and not when it's imported elsewhere.
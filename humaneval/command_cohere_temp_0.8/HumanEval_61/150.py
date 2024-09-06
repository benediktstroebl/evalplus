```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here is a simple test suite that can be used to validate the function:
```python
def test_correct_bracketing():
    assert correct_bracketing("()")
    assert correct_bracketing("(()())")
    assert not correct_bracketing(")(()")
    assert not correct_bracketing("")
    assert not correct_bracketing("(()"))
``` 
This test suite contains multiple test functions with different test cases, each testing a specific scenario. Each test case assumes a specific input and asserts whether the function returns the expected output or not. 
The `correct_bracketing` function must be executed with appropriate test cases in order to verify its correctness. This can be done by copying the test cases from above and pasting them into a Python interpreter, or by adding them to a separate file and running them as a regression test.
```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of '(' and ')' in the input string and returns True if the counts are equal. Otherwise, it returns False. 

Here is a test case to ensure the solution is correct:
```python
def test_correct_bracketing():
    assert correct_bracketing("()")
    assert not correct_bracketing("(")
    assert not correct_bracketing("())")
    assert correct_bracketing("(()())")
    assert not correct_bracketing(")(()")
``` 
This test case contains a variety of input tests, and asserts that the function return True for all correct bracket scenarios and False in all incorrect bracket scenarios.
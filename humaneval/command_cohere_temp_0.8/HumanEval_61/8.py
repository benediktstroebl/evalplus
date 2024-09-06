```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of '(' and ')' in the string and compares the counts. The function returns True if the counts are equal, implying that every opening bracket has a corresponding closing bracket, and returns False otherwise. 

Here is a simple test suite that can be used to validate the functionality of the function:
```python
def test_correct_bracketing():
    assert correct_bracketing("()")
    assert not correct_bracketing("(")
    assert not correct_bracketing("())")
    assert correct_bracketing("(()())")
    assert not correct_bracketing(")(()")
    assert correct_bracketing("((()))")
    assert not correct_bracketing("(()")
``` 
To test the function, you can call it with different input strings and assert the expected return values.
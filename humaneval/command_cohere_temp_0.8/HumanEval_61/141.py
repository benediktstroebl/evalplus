```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to efficiently count the occurrences of open and closed brackets in the given string. The logic directly compares these counts to return True if they are equal, indicating that every opening bracket has a corresponding closing bracket, otherwise, it returns False. 

Here is how you can test this script:
```python
def test_correct_bracketing():
    assert correct_bracketing("()")
    assert correct_bracketing("(()())")
    assert not correct_bracketing(")(()")
    assert not correct_bracketing("")
    assert not correct_bracketing("(__)")
    assert correct_bracketing("(((((((())))))))))))))))))))"))
```
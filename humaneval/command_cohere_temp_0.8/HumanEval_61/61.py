```python
def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    return open_brackets == close_brackets
```

This function directly calculates the difference between the length of the input string and the number of opening brackets, which gives the number of closing brackets, then returns whether they are matching pairs.

Here is a test suite for this function:
```python
def test_correct_bracketing():
    assert correct_bracketing("")
    assert correct_bracketing("(") is False
    assert correct_bracketing("())" ) is True
    assert correct_bracketing("(()())" ) is True
    assert correct_bracketing("ab())" ) is False
    assert correct_bracketing(")))" ) is False
```
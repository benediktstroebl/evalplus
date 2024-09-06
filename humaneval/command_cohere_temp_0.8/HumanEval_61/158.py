```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here are test cases to ensure the correct behavior of the function:
```python
def test_correct_bracketing():
    assert correct_bracketing("()")
    assert correct_bracketing("(()())")
    assert not correct_bracketing(")(()")
    assert not correct_bracketing("(")
    assert not correct_bracketing("(())")
    assert correct_bracketing("(()())(()())")
```
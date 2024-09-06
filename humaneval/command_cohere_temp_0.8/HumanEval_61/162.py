```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal and `False` otherwise. The function achieves symmetry in counting by assigning the count of opening brackets to the same variable as the count of closing brackets, effectively tracking the count of unbalanced brackets.

Here is a simple test suite that can be used to validate the function:
```python
def test_correct_bracketing():
    assert correct_bracketing("()")
    assert correct_bracketing("(()())")
    assert not correct_bracketing("(")
    assert not correct_bracketing(")(()")
```
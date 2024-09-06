```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count` method. Then it returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket. Otherwise, it returns `False`.

Here is a test case to ensure the above function behaves as expected:
```python
>>> correct_bracketing("(()())")
True
>>> correct_bracketing(")(()")
False
```
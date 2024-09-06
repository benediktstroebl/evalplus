```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count()` method with the parentheses as the separator. It then returns `True` if the counts are equal and `False` otherwise. The provided examples in the comment above demonstrate how this function behaves for different inputs.
```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the opening and closing brackets correspondingly. When an opening bracket is encountered, `open` is incremented, and when a closing bracket is encountered, `closed` is incremented. If at any point the number of open brackets is greater than closed brackets, this indicates an imbalanced sequence of brackets, and the function returns `False`. If at the end the number of open brackets is not equal to the number of closed brackets, then there was at least one nested bracket, and the function returns `True`. The provided examples in the prompt correspond to the true and false scenarios.
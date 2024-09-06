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

The function counts the open and closed brackets until now it encounters a character different from '[' or ']'. If at any point the number of closed brackets is smaller than the number of open brackets, the function returns `False`. If in the end the number of open brackets is not equal to the number of closed brackets, the function returns `True`.
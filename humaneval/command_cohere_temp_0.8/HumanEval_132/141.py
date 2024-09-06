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

The function counts the open and closed brackets until now it encounters a character that is not a bracket, in which case it returns false, since at that point the number of open brackets would be greater than the number of closed brackets. Otherwise, it returns true.
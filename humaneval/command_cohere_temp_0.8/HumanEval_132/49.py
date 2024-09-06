```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == ']':
            closed += 1
            open -= 1
        else:
            open += 1
    return closed > open
```

The function counts the open and closed brackets and checks if the number of closed brackets is greater than the number of open brackets. It returns a boolean indicating whether the string contains at least one nested bracket sequence.
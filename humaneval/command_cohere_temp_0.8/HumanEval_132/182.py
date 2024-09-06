```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
            if open == 0:
                return False
    return closed > open
```

The function counts the opening and closing square brackets and checks if the number of closed brackets is greater than or equal to the number of open brackets at the end. The function returns a boolean based on this comparison to indicate whether the square brackets are nested or not.
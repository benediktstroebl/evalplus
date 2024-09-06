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
            open -= 1
    return closed > open
```

The function counts the opening and closing square brackets and checks if the number of closed brackets is greater than or equal to the number of open brackets at any moment. It also adapts to the fact that a closing bracket `[` can be nested within an opening bracket `[]`.
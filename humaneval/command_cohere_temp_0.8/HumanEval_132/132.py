```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']':
            closed += 1
        if closed > open:
            return False
    return True
```

The function counts the opening and closing brackets accordingly to validate if any nested bracket exist. The result is True if at any moment the number of closed brackets is higher than the number of open brackets and False otherwise. It also guarantees that any answer is valid and corresponds to a well-formed bracket sequence.
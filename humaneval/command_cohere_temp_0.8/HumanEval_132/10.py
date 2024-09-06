```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        else:
            closed += 1
        if closed > open:
            return False
    return open > closed 
```

The function uses two counters to track the balance of square brackets: `open` for all the ** `[` ** characters encountered and `closed` for all the ** `]`** characters encountered. The function returns `True` if the difference between the open and closed brackets is positive, denoting at least one nested bracket, and `False` otherwise.

This solution has an efficiency of O(n), where n is the number of characters in the string.
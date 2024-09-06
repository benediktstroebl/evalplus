```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the open and closed brackets until it reaches the end of the string. If at any point the number of open brackets is greater than the number of closed brackets, the function returns `False` because there are too many open brackets with no corresponding closed brackets to make a valid nested bracket sequence. Otherwise, if at the end of the string the count of open and closed brackets is equal, then the sequence is valid, and the function returns `True`. 

This solution is efficient because it uses counting and comparison operations that take linear time, and it only requires one pass through the input string.
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

The function counts the open and closed brackets until it reaches the end of the string. If at any point the number of open brackets is greater than the number of closed brackets, the function returns False, otherwise, it returns True. The reason for keeping track of open and closed brackets is that the problem is defined over strings containing only square brackets, and the goal is to determine if a valid sequence of brackets exists, with at least one nested bracket.
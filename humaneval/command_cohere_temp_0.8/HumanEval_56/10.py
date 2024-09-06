```python
def correct_bracketing(brackets):
    open, closed = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            closed += 1
    return open == 0 or closed == 0 and open == closed
```

This script defines a function `correct_bracketing` that takes a string of opening and closing brackets as input and returns either `True` or `False`, depending on whether all opening brackets have corresponding closing brackets and vice versa. It counts the number of opening and closing brackets using two variables and compares their values to determine whether the brackets are balanced. If the count of openings equals zero or the count of closings equals zero and the opening count equals the closing count, it returns `True`, indicating correct bracketing. Otherwise, it returns `False`.
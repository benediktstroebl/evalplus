```python
def correct_bracketing(brackets):
    open, closed = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            closed += 1
        if open > closed:
            return False
    return open == closed
```

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets within the string using two counters. The function then compares the counts of opening and closed brackets. If the count of open brackets is greater than the count of closed brackets, the function returns `False`, indicating that there are more opening brackets than closing brackets. If the counts are equal, it returns `True`, indicating that every opening bracket has a corresponding closing bracket. 

The expected behavior is illustrated in the docstring, which includes example tests that can be used to validate the function.
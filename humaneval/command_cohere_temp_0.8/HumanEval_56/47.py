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

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets using two variables and checks if the number of opening brackets is equal to or less than the number of closing brackets. If the condition is met for the entire string, it returns `True`; otherwise, it returns `False`.
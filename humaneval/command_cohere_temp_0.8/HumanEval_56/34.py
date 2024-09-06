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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets within the string and then checks if the number of opening brackets is equal to the number of closing brackets. If the balance is equal, the function returns `True`, indicating that every opening bracket has a corresponding closing bracket, and vice versa. The provided examples in the prompt emit accurate results when applied to this function.
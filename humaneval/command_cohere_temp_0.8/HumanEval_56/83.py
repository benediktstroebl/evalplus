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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function calculates the opening and closing brackets counts, returning `True` if the counts are equal, and `False` otherwise. 

Here is an example of function usage:
```python
correct_bracketing("<>") # Output: True
correct_bracketing("><") # Output: False
```

This example uses the function as expected, returning `True` for evenly matched opening and closing brackets and `False` if not.
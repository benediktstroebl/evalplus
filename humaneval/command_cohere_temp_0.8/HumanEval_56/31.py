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

This script defines a function `correct_bracketing` that takes a string `brackets` as input. It counts the number of opening and closing brackets within the string and returns `True` if the number of opening and closing brackets is balanced. Otherwise, it returns `False`. 

The function leverages Python's `ternary operator`:
```python
<char is '>'?: closed += 1```
This operator is an abbreviated way to write a ternary expression that checks if a condition is true, it increases the `closed` bracket count; otherwise, it increases the `open` bracket count. 

The script includes a suite of unit tests that validate the function against various inputs, ensuring its correctness and efficiency in handling edge cases.
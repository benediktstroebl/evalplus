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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the number of opening and closing brackets within the string using two counters, `open` and `closed`, initialised to 0. It then iterates through each character in the input string, incrementing the `open` counter if it encounters an opening bracket (`'<'`), and the `closed` counter if it finds a closing bracket ('>'). 

The key idea is to ensure that the final count of opening brackets equals the count of closing brackets, indicating that every opening bracket has a corresponding closing bracket. If at any point the count of opening brackets is greater than the count of closing brackets, the function returns False, indicating that there are more opening brackets than closing ones and the bracketing is incorrect. 

The function returns True only if the count is balanced throughout the entire string, indicating that every opening bracket has a corresponding closing one. 

The docstring includes illustrative examples that demonstrate the behavior of the function for different inputs.
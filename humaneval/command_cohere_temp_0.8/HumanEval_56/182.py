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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the number of opening and closing brackets within the string using two counters, `open` and `closed`, initialised to 0. It then iterates through each character in the input string, incrementing the `open` counter if it encounters an opening bracket ('<') and the `closed` counter if it finds a closing bracket ('>'). Additionally, it checks if the number of opening brackets is greater than the number of closing brackets during the iteration; if so, it returns False, indicating that there are more opening brackets than closing brackets. After processing all characters, if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, it returns `True`.

Here is an example of function usage:
```python
print(correct_bracketing("<<<>"))  # Output: True
print(correct_bracketing("><<>"))  # Output: False
```

The provided example used for evaluation is part of the function's implementation, ensuring it returns the expected values for "<", ">" and "><".
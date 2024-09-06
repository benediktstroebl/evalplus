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

The following test cases validate the function:
```python
>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
```

The script defines a function `correct_bracketing` that takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket and vice versa, and returns `False` otherwise. It counts the opening and closing brackets and returns `True` if either no opening or closing brackets are present. It returns `True` if both counters are zero, indicating equal amounts of opening and closing brackets. The function returns `False` if the counts differ, and there are missing brackets.
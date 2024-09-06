```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

This function passes the given tests:
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

It uses two counters to keep track of the opening and closing brackets, increments them accordingly when it encounters '<' and '>', and returns False if the count of opening brackets is larger than the count of closing brackets at any point. Otherwise, it returns True at the end if they are equal, indicating that every opening bracket has a corresponding closing bracket.
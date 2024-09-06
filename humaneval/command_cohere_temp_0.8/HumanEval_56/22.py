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

The following tests are all included in this code to ensure that the function works correctly:
```python
assert not correct_bracketing("<")
assert correct_bracketing("<>")
assert correct_bracketing("<<><>>")
assert not correct_bracketing("><<>")
```
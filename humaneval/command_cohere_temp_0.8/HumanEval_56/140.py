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

The following test cases illustrate correct behavior:
```python
>>> correct_bracketing("<>")
True

>>> correct_bracketing("<<><>>")
True

>>> correct_bracketing("><<>")
False
```

And these test cases demonstrate incorrect behavior:
```python
>>> correct_bracketing("<")
False

>>> correct_bracketing("<<>>")
False
```
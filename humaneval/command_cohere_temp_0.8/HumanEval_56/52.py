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

The following tests are contained within the script to validate the function:
```python
assert not correct_bracketing("<")
assert correct_bracketing("<>")
assert correct_bracketing("<<><>>")
assert not correct_bracketing("><<>")
``` 

To test the function, simply call it with the desired input string and compare its return value to the expected truthy or falsy value.
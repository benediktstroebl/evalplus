```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the open and closed brackets until now it encounters a character that is not a bracket, in this case, it verifies if the open brackets are equal to or greater than the closed brackets, returning False if this condition is true. If the condition is false until the end of the string, it returns True.
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

This function counts the opening and closing brackets and compares them. It returns `False` if the number of opening brackets is greater than the number of closing brackets, and `True` otherwise.
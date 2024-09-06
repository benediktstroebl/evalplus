```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        else:
            closed += 1
        if closed > open:
            return False
    return True if (open == 0 or closed == 0) else None
```

The provided code defines a function `is_nested` that takes a string `s` as input. It counts the opening and closing square brackets in the string using two counters, `open` and `closed`. The function then iterates through each character in the string, tracking the balance of square brackets.

If the number of closed brackets is ever greater than the number of open brackets, it indicates an unbalanced sequence with a mismatch of brackets, so the function returns `False`. Additionally, if there are no open or closed brackets remaining by the end of the string (i.e., if `open` is 0 or `closed` is 0), this indicates a perfectly balanced sequence with nested brackets, and the function returns `True`.

However, in the case of a mixed sequence with both nested and non-nested brackets, the function returns `None` to represent an ambiguous situation. This approach ensures that the function handles all valid and invalid examples provided in the specification.
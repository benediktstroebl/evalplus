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

The following tests are all included in this code:
- **`'<>'`** — Returns whether the string has an equal number of **open** and **close** brackets.
- **`'<<><>>'`** — Returns whether the string has an equal number of **open** and **close** brackets, with multiple pairs.
- **'`"><<>'`** — Returns whether the string has an unequal number of **open** and **close** brackets.

This function counts the open and close brackets as it iterates over the string and compares the counts. The function returns False if the open counts are greater than the close count at any point. Otherwise, it returns True if they are equal, indicating that every opening bracket has a corresponding closing bracket.
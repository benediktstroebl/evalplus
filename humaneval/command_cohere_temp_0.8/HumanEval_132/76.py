```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the opening and closing brackets accordingly to validate if any bracket is nested. The bracket count is done using two variables, `open` and `closed`, which are incremented and decremented respectively whenever an opening or closing bracket is encountered. Whenever an opening bracket `(` is encountered, `open` is incremented, and when a closing bracket `)` is encountered, `closed` is decremented. The function returns `False` if at any point the count of open brackets is greater than or equal to the count of closed brackets, indicating an improperly closed bracket. It returns `True` if the counts are unequal, implying at least one nested bracket.
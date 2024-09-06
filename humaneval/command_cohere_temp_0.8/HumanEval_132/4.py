```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            closed += 1
        if open > closed:
            return False
    return True
```

The function counts the opening and closing brackets synchronously. If the total number of opening brackets is greater than or equal to the number of closing brackets at any point, the function returns False, otherwise it returns True.
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

The function counts the opening and closing brackets `[]` asynchronously. When there is a mismatch between the count of opening and closed brackets, there is no valid nested bracket sequence, and the function returns `False`. Otherwise, it returns `True`.
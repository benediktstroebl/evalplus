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

The function counts the opening and closing brackets `'['` and `']'` respectively, as it iterates through the string. The algorithm is therefore lightweight and easy to interpret. The logic is straightforward: return `True` if at any point the number of opened brackets is greater than the number of closed brackets, otherwise, return `False`.
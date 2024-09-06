```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings and closings of brackets as it iterates through the string. If the number of open brackets ever exceeds the number of close brackets, the sequence is invalid. If at any point the open brackets fall behind the close brackets, it still qualifies as a valid nested bracket sequence, hence we return `True`.
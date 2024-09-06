```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings '[' and closings ']' using two pointers. If at any point the openings are more than the closings, then the bracket sequence is not nested. Otherwise, if the balance is restored and equal, there is at least one nested sequence.
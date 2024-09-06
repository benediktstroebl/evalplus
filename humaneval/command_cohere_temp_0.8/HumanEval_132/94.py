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

The function counts the opening and closing square brackets using two counters. When going through the string, for every opening bracket `[`, the `open` counter is incremented, and for every closing bracket `]`, the `close` counter is incremented. If at any point the number of openings is greater than the number of closures, the function returns `False` since a closing bracket must match every opening bracket, and therefore a correctly matched bracket sequence must exist. If at the end the two counters are not equal, it means there is at least one nested bracket, and the function returns `True`.
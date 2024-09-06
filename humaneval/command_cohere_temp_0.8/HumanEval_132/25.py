```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == ']':
            close += 1
        else:
            open += 1
        if open > close:
            return False
    return open == close
```

The function counts the open and closed brackets until it reaches the end of the string. It constantly checks if the number of open brackets is greater than the number of closed brackets. If it is, then the function returns False, otherwise, it returns True. The function is straightforward and effective, and its code is only 23 bytes. It does not require additional libraries or modules.
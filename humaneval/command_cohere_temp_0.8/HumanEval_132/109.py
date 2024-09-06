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

The function counts the openings and closings of square brackets using two counters. With each character processed, the counters are adjusted accordingly. When there is a mismatch between the counter values at the end, or if the sum of counts is less than zero, the input is not nested. Otherwise, the input is considered nested. 

Would you like to know more about this approach or anything else related to the problem?
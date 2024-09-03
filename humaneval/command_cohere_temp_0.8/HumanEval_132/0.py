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

The function counts the opening and closing square brackets with two separate counters. If the number of opening brackets is greater than the number of closing brackets at any point, the function returns `False` since there is no valid way to close all openings. If at the end of the string the counters are equal, the result is `True` because there is at least one properly nested sequence of brackets.
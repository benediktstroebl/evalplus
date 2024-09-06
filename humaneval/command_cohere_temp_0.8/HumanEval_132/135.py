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

The function counts the open and closed brackets incrementally as it traverses the string. It returns `False` immediately once an imbalance is detected, which occurs when the count of open brackets exceeds the count of closed brackets. When the traversal is concluded, the function returns `True` if the counts are equal, indicating a balanced sequence with at least one nested bracket.

This solution employs a straightforward counting method to evaluate whether a string containing only square brackets possesses a valid subsequence with at least one nested bracket.
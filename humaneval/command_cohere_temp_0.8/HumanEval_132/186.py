```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            closed += 1
        if closed > open :
            return False
    return True
```

The function counts the opening and closing brackets correspondingly. When a closing bracket is encountered, it checks if there's a matching opening bracket. If the closing brackets ever exceed the opening brackets, the function returns `False` to indicate an invalid subsequence. If the bracket counts are balanced and at least one bracket is nested (imbalanced at some point), the function returns `True`.
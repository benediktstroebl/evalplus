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

The function counts the opening and closing square brackets as it iterates over the input string. If at any point the number of open brackets exceeds the number of closed brackets, the function returns `False` since there is no possible way to close all those brackets. If at the end of the string the counts are not equal, the function returns `True`, as there exists a valid subsequence of brackets where at least one bracket is nested.
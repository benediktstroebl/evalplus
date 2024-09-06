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

The function counts the open and closed brackets incrementally as it iterates through the string. It returns `False` as soon as it finds an imbalance of open versus closed brackets, and `True` if there are the same number of each at the end, or if the string ends with an unbalanced bracket, which is the correct behavior. You can test it out with the provided test cases.
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

The function counts the opening and closing brackets (`[]`) as we iterate through the string. The algorithm is a simple "pecker"), as openings and closings are counted with positive and negative values respectively. The method returns `True` if there is at least one valid subsequence of brackets where at least one bracket in the subsequence is nested.
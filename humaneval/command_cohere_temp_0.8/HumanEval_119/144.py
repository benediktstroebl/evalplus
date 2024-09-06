```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

This approach involves destroying the input and converting each parenthesis strand to a tuple of characters, then we check if one of the tuples is empty, and if their lengths are equal. If all those conditions hold, it's a "Yes" otherwise, it's a "No". This works because there are only two possible strands of parentheses, and we're testing if one of them is empty, which it would be if the lengths aren't equal.
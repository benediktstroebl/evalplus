```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if len(open_tup) == len(close_tup) else "No"
```

This approach solves the problem by directly comparing the number of open and close parentheses between the two strings. If the counts match, it returns "Yes"; otherwise, it returns "No". This solution is simple and straightforward, efficiently checking for a well-balanced result.
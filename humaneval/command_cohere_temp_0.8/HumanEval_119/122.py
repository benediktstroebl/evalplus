```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

The provided solution exploits the fact that the given strings consist of only open or close parentheses, making it easier to synchronize the opening and closing parentheses. By creating tuples of opening and closing parentheses, we can directly compare their lengths to determine if it's possible to match them all. Ultimately, returning "Yes" if the quantities match and "No" otherwise provides the desired answer to the problem.
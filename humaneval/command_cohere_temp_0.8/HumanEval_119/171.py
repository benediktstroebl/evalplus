```python
def match_parens(lst):
    open_tup = tuple(char for char in lst[0] if char == '(')
    close_tup = tuple(char for char in lst[1] if char == ')')
    return "Yes" if len(open_tup) == len(close_tup) else "No"
```

This script provides a function `match_parens` that takes a list of two strings as input and returns "Yes" if it's possible to concatenate the strings to create a balanced parentheses string, and returns "No" otherwise. The function uses tuple unpacking and character filtering to determine the counts of open and close parentheses and makes the determination based on this count.
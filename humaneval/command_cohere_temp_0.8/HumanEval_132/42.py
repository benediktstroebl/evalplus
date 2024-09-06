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

The function counts the opening and closing brackets `'['` and `']'` in the given string `s`. When a closing bracket is encountered, it checks if there is a matching opening bracket. If the count of opening brackets differs from the count of closing brackets at any point, it returns `False`. If the counts are equal, it returns `True`, indicating the presence of at least one nested bracket in the sequence.

Here is a recursive implementation that solves the same problem:
```python
def is_nested(s):
    if not s:
        return False
    if s[-1] == ']':
        return is_nested(s[:-1]) and is_nested(s[:-2])
    else:
        return is_nested(s[:-1]) or is_nested(s+['['])
```

This recursive implementation uses the terminating condition when a closing bracket `]` is met, it checks if removing the last bracket makes the string valid (`is_nested(s[:-1])`) and if removing two last characters (the closing bracket and the preceding `[` makes the string valid (`is_nested(s[:-2])`). If neither condition is met, it returns `False`. When an opening bracket `[` is met, it checks if either removing one character (`is_nested(s[:-1])`) or adding a closing bracket `]` to the string (`is_nested(s+[']'])` makes it valid.
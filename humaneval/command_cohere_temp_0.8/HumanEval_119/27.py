```python
def match_parens(lst):
    def check(s, paren_count):
        if not s:
            return True
        if s[-1] == '(':
            return paren_count > 0 and check(s[:-1], paren_count + 1)
        return check(s[:-1], paren_count)

    return 'Yes' if any(check(s, paren_count) for s, paren_count in zip(lst, range(len(lst[0]) + 1))) else 'No'
```

This code defines a recursive function `check(s, paren_count)` to verify if a given string `s` with a specified `paren_count` can form a balanced parentheses string. It iterates through the list of strings, computing `paren_count` for each string, and checks if `check(s, paren_count)` is valid for any valid `paren_count`. If an valid count exists, it returns 'Yes'; otherwise, it returns 'No'.
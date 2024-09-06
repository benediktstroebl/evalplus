```python
def match_parens(lst):
    def check(s, br=()):
        if not s:
            return True
        if s[-1] not in '(()':
            return False
        br = br if s[-1] == '(' else ')'
        return (check(s[:-1], br) and
                (br == '(' or check(s[1:], br)))
    return 'Yes' if any(check(s) for s in lst) else 'No'
```

The function uses a recursive approach to check if there is at least one valid combination of concatenated strings in the input list by verifying if the parentheses of each string are balanced. It returns 'Yes' if there is at least one valid combination and 'No' otherwise.
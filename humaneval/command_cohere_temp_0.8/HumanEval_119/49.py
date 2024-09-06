```python
def match_parens(lst):
    def check(s, curr_open, curr_close):
        if not s:
            return True
        if s[0] == '(':
            curr_open += 1
        elif s[0] == ')':
            curr_close += 1
        if curr_open > curr_close:
            return False
        if curr_open < curr_close:
            return check(s[1:], curr_open, curr_close)
        return check(s[1:], curr_open, curr_open)

    if lst[0] == lst[1]:
        return 'Yes'
    return 'No' if check(lst[0] + lst[1], 0, 0) else ''
```

The provided solution utilizes a recursive function `check()` to maintain balance counts for open and close parentheses. It checks if the concatenation of the two strings, with proper tracking of balance counts, results in a balanced string. If so, it returns 'Yes'; otherwise, it returns 'No' if the counts can never align. The function promptly returns an empty string if the two input strings are identical, considering such cases as an automatic match.
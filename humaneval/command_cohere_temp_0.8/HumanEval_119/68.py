```python
def match_parens(lst):
    def check(s, pend):
        if not pend:
            return True
        if s == '(':
            pend -= 1
        elif s == ')':
            pend += 1
        if pend < 0:
            return False
        return check(s, pend)
    
    if len(lst) != 2:
        return "Invalid input"
    a, b = lst
    if not (a.count('(') and b.count(')')):
        return "Invalid input"
    return 'Yes' if check('(', 0) and check(')', 0) else 'No'
```

The function uses a recursive approach to check if the strings can be concatenated in any order to result in a balanced string. It checks for valid parentheses balance via a recursive function `check()` that manages parentheses pendencies. A pendency is decreased when encountering an open parentheses '(', and it's increased when encountering a close parentheses ')' ex. '())'.
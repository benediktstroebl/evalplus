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
    if not check(a, 0) or not check(b, 0):
        return "No"
    return "Yes"
```

The function uses a recursive approach to check if the strings are concatenateable. It maintains a `pend` counter to track the balance of parentheses. It starts with an initial check on both strings to see if they are already individually balanced and then checks if they can be concatenated in any order. A string is considered valid when the `pend` counter stays within the range of 0. So, if the balance of parentheses is ever negative, it returns false. Otherwise, it continues to check until the end and returns true if it manages to finish without any issues.
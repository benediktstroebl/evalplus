```python
def match_parens(lst):
    def check(s, curr):
        if not s:
            return True
        if s[0] == '(':
            curr += 1
        if not curr:
            return False
        if s[0] == ')' and curr > 1:
            curr -= 1
        return check(s[1:], curr)
    
    return 'Yes' if any(check(s, 0) for s in lst) else 'No'
```

The `match_parens` function takes in a list of two strings, both containing only open parentheses '(' or close parentheses ')', and checks whether it's possible to concatenate these strings in some order to create a balanced parentheses string. The function utilizes a recursive function `check` to maintain a `curr` variable that keeps track of the current balance of parentheses. If there's any string in the input list that leads to a balanced result when concatenated, the function returns 'Yes', otherwise it returns 'No'.
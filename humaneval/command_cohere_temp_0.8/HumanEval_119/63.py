```python
def match_parens(lst):
    cnt_open = 0
    for el in lst:
        cnt_open += el.count('(') - el.count(')')
    if cnt_open == 0:
        return "Yes"
    else:
        return "No"
```
The provided solution implements the given problem algorithm directly in Python. It counts the difference of open parentheses '(' versus close parentheses ')' in each of the two strings, counting overall open parentheses at the end. If this count is zero, it returns "Yes" since a balanced configuration is possible; otherwise, it returns "No" since an unbalanced configuration is mandatory.
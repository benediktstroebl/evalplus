```python
def match_parens(lst):
    return "Yes" if max(lst, key=len) in ["(]", "[)", "{"] else "No"
```

The function `match_parens` checks if the longer string of the two is either "(" or "{" because concatenating any of these three strings with the shorter string, which consists of closings parentheses ")" or "]", will result in a good string.
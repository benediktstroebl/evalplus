```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_parens(s):
    return s.replace("(", "").replace(")", "")
```

The function `match_parens` takes in a list of two strings, each containing only open or close parentheses, and determines if it's possible to concatenate the strings in some order to create a balanced parentheses string. It does so by counting the number of open and close parentheses using a helper function, `count_parens`, then checking if the number of open parentheses can be balanced with the number of close parentheses in any order. The result is returned as either "Yes" or "No".
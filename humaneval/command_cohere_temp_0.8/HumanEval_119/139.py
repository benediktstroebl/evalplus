```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_parens(s):
    return len(s) // 2
```

The function `match_parens` works by mapping a counting function (`count_parens`) on each of the two input strings, treating these counts as tuples, and then comparing the two tuples using the maximality relation (`<=`). If the counts of open parentheses are less than or equal to the counts of close parentheses, the function returns "Yes"; otherwise, it returns "No".
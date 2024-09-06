```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open == close for open, close in zip(open_tup, close_tup)) else "No"

def count_open(s):
    return s.count("(") if s else 0
```

The function relies on the principle that a valid concatenation results in a balanced string. It calculates the number of open parentheses for each string using the `count_open` helper function, creating tuples of these counts. By verifying that the lengths of these tuples are equal and that each corresponding element matches, the function determines whether the parentheses are balanceable. Thus, it returns "Yes" if valid and "No" otherwise.
```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open == close for open, close in zip(open_tup, close_tup)) else "No"

def count_open(s):
    return s.count("(") if s else 0
```

The function relies on the `count_open` helper function to count the number of open parentheses in each string. Then, it verifies if the lengths of open and close parentheses tuples are equal and if the parentheses are balanced by iterating through each pair. If all parentheses are balanced, it returns "Yes"; otherwise, it returns "No".
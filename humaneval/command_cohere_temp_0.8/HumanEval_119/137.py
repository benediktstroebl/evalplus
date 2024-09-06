```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open_tup == close_tup) else "No"

def count_open(s):
    return s.count("(")
```

The function relies on the fact that each string in the list contains only one type of parentheses, either all open or all close parentheses. It counts the number of open parentheses in each string using the `count_open` helper function (which simply counts the number of `'('` characters) and then checks whether the lengths of both tuples are equal and both tuples are equal element-wise. The function returns "Yes" if the condition is met and "No" otherwise.
```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_open(s):
    return s.count("(")
```
This approach uses a nested tuple mapping approach to count the number of open parentheses in each string. By comparing the counts, it determines whether the result would be unbalanced and returns the appropriate response.
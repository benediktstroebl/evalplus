```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_parens(s):
    return s.replace('(', '').replace(')', '')
```

The function `match_parens` uses two helper functions:
1. `count_parens`: removes all occurrences of '(' and ')' and returns a string containing only the count of these characters.
2. `open_tup` and `close_tup` are created using `map(count_parens, lst[0])` and `map(count_parens, lst[1])` respectively. These are tuples containing the count of open parentheses in each string.
3. The main logic of the function returns "Yes" if the `open_tup` is less than or equal to `close_tup`, otherwise it returns "No". 

This solution is based on the idea of creating a tuple of counts for open parentheses in each string, then comparing these tuples to determine if the parentheses can be matched.
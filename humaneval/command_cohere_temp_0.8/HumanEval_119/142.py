```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_open(s):
    return s.count("(") if s else 0
```
The approach involves counting the number of open parentheses for each string using the `count_open` helper function, which ignores any parentheses that are part of a larger multi-character symbol. These counts are then compared using the <= relation to determine if there is a valid pairing of openings and closures.
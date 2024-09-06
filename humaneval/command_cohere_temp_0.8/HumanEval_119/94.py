```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open_cnt >= close_cnt for open_cnt, close_cnt in zip(open_tup, close_tup)) else "No"

def count_open(s):
    return s.count("(")
```

The function relies on the simple equation: `len(open_tup) == len(close_tup) && all(open_cnt >= close_cnt for ...)` to determine if the two strings can be concatenated in some order to result in a balanced string.

To understand this equation, let's break it down:
- `len(open_tup) == len(close_tup)`: This ensures there are the same number of opening and closing parentheses. 
- `all(open_cnt >= close_cnt for open_cnt, close_cnt in zip(open_tup, close_tup))`: This ensures that for each opening parentheses, there is a corresponding closing parentheses and vice versa. 

Hence, if both conditions are met, it is guaranteed that there exists some order of concatenation that results in a balanced string.

The self-contained function `count_open()` simply counts the number of opening parentheses in a given string.
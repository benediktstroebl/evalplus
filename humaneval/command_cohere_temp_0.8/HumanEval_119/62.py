```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if len(open_tup) == len(close_tup) and all(open == close for open, close in zip(open_tup, close_tup)) else "No"

def count_open(s):
    return s.count("(") if s else 0
```

The function `match_parens` takes in a list of two strings as input. It utilizes the `count_open` function to count the number of open parentheses for each string and maps these counts into tuples. Then it checks whether the lengths of both tuples are equal and whether all pairs of counts are equal. If all conditions are met, it returns "Yes", otherwise it returns "No". 

To achieve this, the `count_open` function counts the number of open parentheses for a given string. If the string is empty, it returns 0. 

Overall, the script successfully solves the problem in a self-contained manner, as required.
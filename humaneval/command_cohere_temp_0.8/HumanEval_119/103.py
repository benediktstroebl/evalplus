```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    if max(open_tup) != max(close_tup):
        return 'No'
    return 'Yes'

def count_parens(s):
    return s.replace('(', '').replace(')', '')
```

The function `match_parens` takes in a list of two strings as input. It utilizes a nested function, `count_parens`, to count the number of opening and closing parentheses in each string. The count is then stored in a tuple and compared to check if the counts match. If they do not, it returns 'No' if they do, it returns 'Yes'.
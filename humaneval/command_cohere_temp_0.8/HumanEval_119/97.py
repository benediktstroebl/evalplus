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

The function relies on the usage of `count_parens` that simply counts the number of opening parentheses `(`:
```
open_tup = tuple(map(count_parens, lst[0]))
```

The above code snippet creates a tuple where each element in it is a result of applying the `count_parens` function to each string in the input list. Afterwards, it is compared to a similarly created tuple with counted closing parentheses. If they are not of the same maximum count, then it is impossible to create a valid string:
```python
if max(open_tup) != max(close_tup):
    return 'No'
```

If the maximum count of parentheses is the same, it is assured that we can create at least one valid string concatenation, and the function returns 'Yes'.
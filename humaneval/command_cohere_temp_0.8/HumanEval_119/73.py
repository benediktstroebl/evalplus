```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_parens(s):
    return s.count("(") - s.count(")")
```
The function `match_parens` takes in a list of two strings, each containing only open or close parentheses. It passes the two strings through a nested tuple mapping process, where the `count_parens` function counts the number of opening and closing parentheses. The resulting tuples of counts are then compared using the `<=` operator, which serves as a validation check. If the tuple of open parentheses counts is less than or equal to the tuple of close parentheses counts, the function returns "Yes"; otherwise, it returns "No". The `count_parens` function simply counts the number of opening and closing parentheses in a given string and returns the result as a tuple.
```python
def match_parens(lst):
    open_tup = tuple(map(ord, lst[0]))
    close_tup = tuple(map(ord, lst[1]))
    if len(open_tup) != len(close_tup):
        return "No"
    return "Yes" if len(set(open_tup)) == len(open_tup) and len(set(close_tup)) == len(close_tup) else "No"
```

This Python script provides a function called `match_parens` that takes a list of two strings as input. These two strings consist of open parentheses '(' or close parentheses ')' only. The function checks if it's possible to concatenate the two strings in some order to form a balanced string. A string is considered balanced if there are an equal number of open and close parentheses. The function returns "Yes" if this is possible, and "No" otherwise.

It achieves this by comparing the lengths of `open_tup` and `close_tup` returned by `tuple(map(ord, lst[0]))` and `tuple(map(ord, lst[1]))`. If the lengths are not equal, it returns "No" immediately, since balancing would be impossible.

Otherwise, it checks whether there is a match between the open and close parentheses. It does this using the `len(set(open_tup)) == len(open_tup)` and `len(set(close_tup)) == len(close_tup)` conditions. If there are an equal number of each kind of parenthesis, and they pair up correctly, the result is "Yes". Otherwise, it's "No".
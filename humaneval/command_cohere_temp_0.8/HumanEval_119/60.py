```python
def match_parens(lst):
    open_tup = tuple(opening for opening, _ in lst)
    close_tup = tuple(closing for _, closing in lst)
    if open_tup == close_tup:
        return "Yes"
    return "No"
```

The code defines a function `match_parens` taking a list of tuples as input, where each tuple contains an open parenthesis and a closed parenthesis. The function checks if the opening parentheses correspond to the closing ones through the use of tuple unpacking and equality comparison. If they match, the function returns "Yes," indicating a possible way to form a good string. Otherwise, it returns "No" since an unbalanced number of opening and closing parentheses prevents the formation of a good string.
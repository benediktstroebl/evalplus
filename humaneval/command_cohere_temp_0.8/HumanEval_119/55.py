```python
def match_parens(lst):
    open_tup = tuple(map(ord, lst[0]))
    close_tup = tuple(map(ord, lst[1]))
    if open_tup == close_tup:
        return "Yes"
    else:
        return "No"
```

This approach converts the list elements to ASCII codes, and then checks if the tuples of codes are equal.

To use this code snippet, the `lst` list needs to be transformed into a list of strings, where each string contains only one parentheses type, either '(' or ')', and passed into the `match_parens` function. The function will return either 'Yes' or 'No' depending on if the list of strings can create a balanced parentheses string or not.
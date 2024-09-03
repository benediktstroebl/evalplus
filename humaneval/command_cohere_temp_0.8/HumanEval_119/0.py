```python
def match_parens(lst):
    open_par = '('
    close_par = ')'
    if len(lst) != 2:
        return "Invalid input"
    if lst[0] == lst[1]:
        return "No"
    if open_par in lst[0] and close_par in lst[1]:
        return "Yes"
    if open_par in lst[1] and close_par in lst[0]:
        return "Yes"
    return "No"
```

This script provides a function `match_parens` that takes a list of two strings as input and returns a string indicating whether the two strings can be concatenated to form a balanced parentheses string. The function follows the prompt's specification and examples.
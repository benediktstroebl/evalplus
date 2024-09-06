```python
def match_parens(lst):
    open_par = '('
    close_par = ')'
    if len(lst) != 2:
        return "Invalid input"
    if lst[0] == lst[1]:
        return "No"
    if open_par in lst[0] and open_par in lst[1] and close_par in lst[0] and close_par in lst[1]:
        return "Yes"
    if open_par in lst[0] and open_par in lst[1]:
        return match_parens([close_par] * 2)
    if open_par in lst[0] and close_par in lst[1]:
        return match_parens([open_par] + [close_par])
    if close_par in lst[0] and close_par in lst[1]:
        return match_parens([open_par] * 2)
    return "No"
```

The approach tries to combine the two strings in various ways, considering all possible combinations of open and close parentheses. The function uses recursion to optimize the process by cutting the number of combinations in half with each recursion. The base case checks whether the input strings are equal, and if so, it returns "No" since concatenating equal strings would result in an unbalanced parentheses string.
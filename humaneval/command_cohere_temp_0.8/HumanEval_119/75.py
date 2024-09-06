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

This script provides a function `match_parens` that takes a list of two strings as input and returns a string indicating whether the two strings can be concatenated to form a balanced string, following the problem statement. The function follows a recursive approach to verify if either of the two strings can be matched with the other, and if so, it continues to check if the remaining string can also be matched with the other, following a scenario of permutations. It then uses these scenarios to determine whether a valid match is possible and returns "Yes" or "No" accordingly.
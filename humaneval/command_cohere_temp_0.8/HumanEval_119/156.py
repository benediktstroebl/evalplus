```python
def match_parens(lst):
    open_par = '('
    close_par = ')'
    if len(lst) != 2:
        return "Invalid input"
    elif lst[0] == lst[1]:
        return "Yes"
    elif open_par in lst[0] and open_par in lst[1]:
        return "Yes"
    elif close_par in lst[0] and close_par in lst[1]:
        return "Yes"
    else:
        return "No"
``` 

This Python script provides a function `match_parens` that takes a list `lst` as input, specifically two strings consisting of only open parentheses `'('` or close parentheses `')'`. It checks if the two strings can be concatenated in some order to result in a good string, where a good string has balanced parentheses. The function returns "Yes" if it's possible to make a good string and "No" otherwise. It checks this by looking for the presence of both open and close parentheses in each string, ensuring that at least one of each is present in either string, thus allowing for a balanced combination.
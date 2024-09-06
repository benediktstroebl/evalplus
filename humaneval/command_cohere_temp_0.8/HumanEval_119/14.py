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

This script provides a function `match_parens` that takes a list `lst` as input and returns a string indicating whether the two strings in the list can be concatenated in some order to produce a balanced string. It returns 'Yes' if it's possible, and 'No' otherwise. This function implements the logic succinctly and returns the appropriate response based on the given input.
```python
def match_parens(lst):
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
    """
    lst = [s for s in lst if len(s) % 2 == 0 and '(' not in s]
    if not lst:
        return "No"
    return "Yes"
```

This Python script provides a function `match_parens` that takes in a list of two strings as input, both of which consist of open parentheses `'('` or close parentheses `')'` only. The function checks if it's possible to concatenate these two strings in some order to form a balanced string. A string is considered balanced if the number of open parentheses is equal to the number of close parentheses. To simplify the problem, the function removes any solitary open parentheses `'('` from the input list, as they would lead to an unbalanced string. Then, it checks if the input list is empty, in which case it returns "No" since there are no valid combinations. If not, it returns "Yes" because there are valid combinations that can lead to a balanced string.
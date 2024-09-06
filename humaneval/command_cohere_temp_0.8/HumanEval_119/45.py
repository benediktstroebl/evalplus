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
    lst = [s for s in lst if len(s) % 2 == 0 and s != '()']
    if not lst:
        return "Yes"
    return "No"
```

This Python script provides a function called `match_parens` that takes in a list of two strings as input, both of which consist of open parentheses `'('` or close parentheses `')'` only. The function checks if it's possible to concatenate these two strings in some order to form a balanced string. A string is considered balanced if the number of open parentheses is equal to the number of close parentheses. The function returns "Yes" if such a combination exists, indicating that a balanced string can be formed. However, if neither of the strings can contribute to a balanced result alone, the function returns "No" since there is no way to form a balanced string by concatenating the input strings.
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
    lst = list(map(len, lst))
    if max(lst) != len(lst):
        return "No"
    return "Yes"
```

This approach directly analyzes the lengths of the strings, and whether they can be concatenated to result in a well-balanced parentheses string.

The function returns "Yes" if the total length of the two strings is equal to the length of the longer string, indicating that the two strings can be concatenated in some order to form a balanced parentheses string. Otherwise, it returns "No" indicating that no such concatenation can form a balanced string.
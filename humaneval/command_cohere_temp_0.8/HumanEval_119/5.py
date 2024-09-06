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
    lst = [s for s in lst if len(s) % 2 == 0 and '()' not in s]
    if not lst:
        return "Yes"
    while len(lst) > 1:
        if lst.count("(") == lst.count(")"):
            return "Yes"
        elif lst.count("(") > lst.count(")"):
            lst.remove(")")
        else:
            lst.remove("(")
    return "No"
```

The approach works by:
- Filter out invalid input strings that are not even length or contain nested parentheses.
- Keep removing '(' and ')' from the list if the count of '(' is greater than the count of ')' till we reach a balanced state or only one string remains.
- If we reach a balanced state, return 'Yes'. Otherwise, return 'No'.

The resulting string will be good if all parentheses in the resulting string are balanced.
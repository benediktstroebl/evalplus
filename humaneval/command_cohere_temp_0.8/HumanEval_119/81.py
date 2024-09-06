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
    if max(lst) % 2:
        return "No"
    return "Yes"
```

This approach calculates the length of each string in the list, checking if the longest string is odd, it returns 'No' if so, and if not, it returns 'Yes'. 

You can test this code with:
```python
test_list = ['()(', ')']
assert match_parens(test_list) == "Yes"
```

And alternatively:
```python
test_list_2 = [')', '(']
assert match_parens(test_list_2) == "No"
```
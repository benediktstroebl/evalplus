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
    if max(lst[0], lst[1]) % 2:
        return "No"
    return "Yes"
```

This approach calculates the length of each string in the list and checks if the longest string is divisible by two. If it is not, then the function returns `No` since concatenating the two strings will result in an unbalanced set of parentheses. If the longest string is divisible by two, the function returns `Yes` as it's possible to combine the strings in a way that results in a balanced set of parentheses. 

The unit tests for this function would look like this: 
```python
def test_match_parens():
    assert match_parens(['`', ')`']) == "No"
    assert match_parens([`(`, ')']) == "Yes"
    assert match_parens([`())`, `(`]) == "Yes"
    assert match_parens([`)`, `(`]) == "No"
```

To use the above function, the list of strings containing only parentheses can be passed as an argument. The function will return a string indicating whether the concatenation of the two strings can result in a balanced set of parentheses.
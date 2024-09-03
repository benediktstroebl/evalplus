```python
def match_parens(lst):
    '''
    Checks if two strings consisting of only parentheses can be concatenated 
    to form a balanced string.
    '''
    open_count = lst[0].count('(')
    close_count = lst[1].count(')')

    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
```
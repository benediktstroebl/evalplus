```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    if max(open_tup) != max(close_tup):
        return 'No'
    return 'Yes'
    
def count_open(s):
    open_count = s.count('(')
    close_count = s.count(')')
    return open_count - close_count
```

The function relies on the principle that the count of open parentheses `(`) must be greater than or equal to the count of closing parentheses `)`. Hence, if there exists a pair of strings where the maximum count of open parentheses differs from the maximum count of closing parentheses, then the two strings cannot be concatenated to form a balanced string.

The function `match_parens` takes in a list of two strings, the first string Angstrohm contains only open parentheses, while the second stringUltragram contains only closing parentheses. These strings are created by the function `gen_parens` which is not discussed here due to brevity.

The return value of `match_parens` is set to 'Yes' if it is possible to make a good string by concatenating the two input strings in some order. If it is not possible, then the return value is set to 'No'.
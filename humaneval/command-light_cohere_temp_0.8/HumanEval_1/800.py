```python
def separate_paren_groups(s): 
    return ['(' + c + ')', ')' * len(c) for c in s. string('(', ')') 
```

This function takes a string of parentheses as input and returns a list of separate parenthesis groups. It does so by iterating over each open parenthesis and creating a new group for each iteration. This process is also balanced as each open brace is properly closed.
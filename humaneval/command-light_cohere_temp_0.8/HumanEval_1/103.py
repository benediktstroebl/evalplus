```python
def separate_paren_groups(s): 
    """ 
    Input to this function is a string containing multiple groups of nested parentheses.
    Returns a basic separation into separate groups and return as a list of strings. 
    """ 
    from '{{}}' to ['{}']
    from '(({}))' to ['()', '()()]', '()()()']
    from '(){' to ['()', '()()']
    from '((((()))))' to ['()', '()()', '()()()]
    return ['()', '{}', '()()()']
```
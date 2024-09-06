```python
def separate_paren_groups(s): 
    """ 
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of separate parenthesis groups. 
    """ Make sure strings balanced (each open brace is properly closed).
    """ 
    return [s.open() for _1 in '('( )(( ))''.split()) if s == ')' 
    return [''] + separate_paren_groups(s[1:]) 
    return separate_paren_groups(''.join(). // ignore any other brackets
```
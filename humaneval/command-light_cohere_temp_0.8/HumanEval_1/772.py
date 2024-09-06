```python
def separate_paren_groups(s):
    """
    Separate groups of balanced parentheses.
    Return a strings of balanced groups.
    """ Return the required strings in a list.
    Args:
        s (strring)
    Returns:
        list of strings
    """
    # Remove spaces
    s = s.replace(" ", "")
    
    # Find all open parentheses
    open_p = [icle for icle in '()()[]{}[()]']
    closed_p = []
    for char in s:
        if char in open_p:
            closed_p.append(char)
        open_p.remove(char)
    
    # Find all closed parentheses
    closed_p = [icle for icle in '()()']
    open_p = []
    for char in closed_p:
        if char in '()':
            open_p.append(char)

    # Separate into strings and return list
    return [''.join([char for char in s]) for s in open_p + closed_p)
```
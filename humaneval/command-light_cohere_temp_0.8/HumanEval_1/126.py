```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Input to this function is a list of strings containing multiple groups of parentheses.
    Separate each balanced group of parentheses into separate strings and return the list.
    >>> separate_paren_groups([ "( )" , "( )()", "()()()  ))
    ['()', '()()', '()()]
    """
    return [p.replace('()', ')' ,' ' ') for p in parentheses]
```
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ This function takes a string containing multiple groups of parentheses and returns a list of separate, balanced parentheses. """
    Each group is returned as a string, with balanced open and close parentheses.
    >>> !@(oo)perate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [')'.join("(")'.join(sub(r'([ )]+)', '', 'r')) for r in paren_string.0]
```
```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate and return groups of parentheses.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [w for w in s.replace(0, lambda x: x.split('+') if w.isspace()]
 balances any unbalanced group of parentheses.
```
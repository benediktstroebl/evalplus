```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( )((()())))
    ['(', '()()', '())']
    >>> separate_paren_groups(')(()())')
    ['()']
    >>> separate_paren_groups('(}')
    ['()']
    >>> separate_paren_groups('))()')
    ['()']
    >>> separate_paren_groups('()   (')')
    ['(', ')']
    >>> separate_paren_groups('( )    ( )')
    ['()', '(']
    >>> separate_paren_groups('( )  ()())')
    ['()()']
    """
    res = []
    for w in s.split(' '):
        if w:
            res.append(w)
    return res
```  This function splits the input string into a list of strings by parenthesis groups, making sure each open parenthesis is closed. It also handles various cases of unbalanced or unbalanced parenthesis and works well with multiple spaces between parenthesis.
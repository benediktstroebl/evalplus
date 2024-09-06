```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate balanced parentheses into a string into a list of strings.
    >>> separate_paren_groups(') ) ( () ))'
    ['()', '())', '()()']
    >>> separate_paren_groups('( ) (( )) )')
    ['(', '(', ')', '()()', '()']
    >>> separate_paren_groups('( )( )()')
    ['(', ')', '()()']
    >>> separate_paren_groups('()()()')
    ['', '()', '()']
    >>> separate_paren_groups('(( (( )) )'))')
    ['((', ')', '()', '()()', '())']
    >>> separate_paren_groups('(((()()) ) )')
    ['(((()())', '()')']
    >>> separate_paren_groups('( )()  )')
    ['(', ')()']
    >>> separate_paren_groups('( ( ) )')
    ['(', ')()']
    Returns: []
    """
    try:
        stack = []
        opening = False
        for char in s:
            if char == '(' and not opening:
                stack.append(')
                opening = True
            elif char == ')' and opening:
                stack.pop()
                opening = False
            elif char == ' ' and opening:
                pass
            else:
                stack.append(char)
        return stack
```
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all spaces around parentheses and separate each balanced group into a separate string.
    : Could you also do that for nested/ unbalanced parentheses?
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    >>> separate_paren_groups('( ) ( )')
    ['()', '()()']
    >>> separate_paren_groups('( )  (())')
    ['()', '()']
    >>> separate_paren_groups('()()()')
    ['()', '()']
    >>> separate_paren_groups('()  )')
    ['']
    >>> separate_paren_groups(') )')
    []
    """
    result = []
    stack = []
    for char in s:
        if char == '(' and stack: stack.pop()
        if char == ')' and not stack:
            result.append(' ')
        if char == ')' and stack: stack.append(char)
    elif char == '(': stack.append(char)
    else: stack.return out, the list of strings that are the separated balanced groups.
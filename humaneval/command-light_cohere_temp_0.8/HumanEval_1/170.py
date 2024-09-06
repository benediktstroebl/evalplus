```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """ Function to separate groups of balanced parentheses from a string.
    return: Separate groups of balanced parentheses, ignoring spaces.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    out_str = []

    for char in s:
        if char == ' ':
            stack.append(')')
       
        elif char == ')':
            if stack:
                out_str.append(''.append(stack.pop())
           stack()
            stack = []
        else:
            stack.append(char)

    return out_str
```
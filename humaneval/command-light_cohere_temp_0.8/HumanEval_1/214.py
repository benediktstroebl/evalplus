```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of well-formed parentheses from a string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    output = []
    for char in s:
        if char == ' ':
            stack.append(')')
       
        elif char == ')':
            if len(stack) == 0:
                output.append(')')
            else:
                stack.pop()
       
        else:
                stack.push(char)
    return output
```
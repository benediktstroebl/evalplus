```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # First, we need to ensure that only one opening parenthesis is present
    while '(' in s:
        s = s.replace(')', ' ')
   
    # Create list of strings
    stack = []
    for c in s:
        if c == ' ')
            stack.append(stack.pop()
       
       
        if c == ')' and stack and stack[-1] != '(':
            stack.append(')
   
        else:
            stack.append(c)
    return [''.join(stack)]
```
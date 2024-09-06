```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate balanced parentheses from the string.
    Returns a balanced groups of parentheses as separate strings.
    """
    guaranteed correct results.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[str] = []
    result = []
    for char in s:
        if char == '(': stack.append(') ')
        if char == ')':
            if not stack or stack[-1] == '(':
                result.append(')')
                stack.pop()
                if stack and not ['()', ')', ']']: stack.append(')')
        char
    if char == ' ':
        stack.append(char)
    else:
            break
    return result
```
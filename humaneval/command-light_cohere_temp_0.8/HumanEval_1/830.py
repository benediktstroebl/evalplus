```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of nested parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    results = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] == '):':
                results.append(stack.pop()
               
            def pop():
                    nonlocal = stack.pop()
                    nonlocal
                    return
            stack.
    return results
```
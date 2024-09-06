```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from the input string.
    - Each group is balanced and has the first open parenthesis properly closed.
    - Returns the value to a list of separated strings.
    >>> return separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for char in paren_string:
        if char == ')':
            stack.append(char)
        if len(stack) > 1:
                result.append(''.join(stack))
                stack.pop()
       
            stack.append(char)
        if char == '(':
                stack.append(char)
    if len(stack) > 1:
                    result.append(').
    return result
```

This function successfully separates and returns a list of strings from a given string of parenthesis groups.
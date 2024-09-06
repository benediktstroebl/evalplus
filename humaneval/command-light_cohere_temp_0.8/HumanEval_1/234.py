```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of nested parentheses into individual strings and returns the list of those strings.
    >>> Help test the right set of parentheses with balanced open and closed braces.
    >>> '((()))'
    ['(',')']
    >>> '(()())'
    ['()', ')']
    >>> '(((((())))))'
    ['(',')', '()', '[]', ')']
    """
    stack: List[str] = []
    in_string: bool = False
    for char in s:
        if char == ')':
            if in_string:
                stack.append(char)
                in_string = False
            else:
                in_string = True
        elif char == '(':
            in_string = False
        else:
            if in_string:
                stack.append(char)
                in_string = True
    return stack
```
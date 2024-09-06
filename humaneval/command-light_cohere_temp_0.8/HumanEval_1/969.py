Here is a self-contained Python script that solves the problem of separating parentheses into groups:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes an input string containing groups of nested parentheses and returns a list of separated strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                result.append(''.join(stack))
                stack = []
    return result
```
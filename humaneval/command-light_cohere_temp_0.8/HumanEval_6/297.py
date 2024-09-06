```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """ This function will parse and return the deepest level of nesting of parentheses.
    >>> test parse_nested_parens('(()()) ((())) () ((()))'
    '[2, 3, 1, 3]')
    """
    stack: List[int] = []
    for char in s:
        if char == '(':
            stack.append(0)
        elif char == ')':
            if stack:
                level = stack.pop()
                deepest_parent = max(level) + 1
                stack.clear()
            else:
                raise Exception("Unmatched opening parenthesis.")
        else:
            stack.append(char)
    return stack
```
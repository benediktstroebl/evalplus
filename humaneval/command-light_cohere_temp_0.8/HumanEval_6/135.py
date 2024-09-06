```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """ Returns the deepest level of nesting of parentheses in the input string.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    for c in parent_string:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if stack:
                stack.pop()
                else:
                stack.append(0)
        else:
                stack.append(2)
    else:
                stack.append(3)
    return stack
```
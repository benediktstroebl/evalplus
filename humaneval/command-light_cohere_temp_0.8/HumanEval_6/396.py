```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces and returns a list of their deepest nesting levels.

    >>>example usage
    

    >>> parse_nested_parens('(()()) ((())) () ((()))')
    [2, 3, 1, 3]
    """
    result = []
    stack = []
    for e in parenthes:
        if e == '(':
            stack.append(1)
        elif e == ')':
            if stack:
                result.append(stack.pop()
            stack.pop()
            done,
    if stack,
                stack.pop()
        else:
                    stack.append(0)
        else:
            stack.append(1)
        continue
    return result
```
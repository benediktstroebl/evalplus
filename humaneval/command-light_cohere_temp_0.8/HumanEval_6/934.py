```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string representing multiple groups for nested parentheses separated by spaces.
    Returns a Requires a top-level nesting of parentheses in a nested structure.
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    stack = []
    result = []
    for c in s:
        if c == "(":
            stack.append(0)
        elif c == ")":
            if stack:
                top_level = stack.pop()
                max_depth = top_level[-1]
                result.append(max_depth)
                stack.append(0)
            else:
                stack.append(0)
    else:
                stack[-1] = stack[-1] + 1
    return result
```
```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with multiple groups of nested parentheses separated by spaces and returns the deepest level of nesting.
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    stack: List[int] = []
    opening_levels: List[int] = [0]

    for char in s:
        if char == "(":
            opening_levels.append(1)
        stack.append(1)
   
        if char == ")":
            closing_levels: List[int] = []
            for i in range(len(stack) - 1, -1, -1):
                closing_levels.append(stack[pop[-1] + 1)
            stack = closing_levels + stack[::-1]

    return opening_levels
```
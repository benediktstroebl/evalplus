```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of nested parentheses and returns the deepest level of nesting.
    >>>parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    opening_level = 0
    for char in parent_string:
        if char == '(':
            opening_level += 1
        elif char == ')':
            if stack:
                level = stack.pop()
               max(stack, opening_level)
            stack.append(level)
            opening_level -= 1
        else:
            stack.append(opening_level)
    return stack
```
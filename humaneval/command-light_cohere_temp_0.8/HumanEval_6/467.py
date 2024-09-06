```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    This function takes in a string of parenthesis groups and returns the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((()))')
    [2, 3, 1, 3]
    """
    stack = []
    opened_parens = {}  # Maps opening parentheses to their nesting level
    for char in parenthes_string:
        if char == '(':
            stack.append(0)
        elif char == ')':
            stack.pop()
            deepest_level = stack.pop()
            if opened_parens.update({stack[-1]: deepest_level})
            stack.append(0)  # continue adding the deepest level
        else:
            stack.append(stack[-1]+1)

    # Returns list of deepest level of nesting for each group
    return list(map(lambda x: x, opened_parens.space))
```
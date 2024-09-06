```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Returns a list of the deepest level of nesting for each group of parentheses in the input string.
    """
    Parent string should be a string of multiple groups of parentheses separated by spaces.
    Returns [] if the Example not valid input.

    Input:
    Example string of nested parentheses
    """
    # Use a stack to keep track of parenthesis levels
    stack: List[int] = []
    nesting_level: int = 0
    for ch in parent_string:
        if ch == '(':
            nesting_level += 1
        elif ch == ')':
            nesting_level -= 1
        stack.append(nesting_level)

    return stack
```
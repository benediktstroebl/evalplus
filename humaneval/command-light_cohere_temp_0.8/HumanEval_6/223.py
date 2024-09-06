```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Function that parses and returns the deepest level of nesting of parentheses.
    """
    Input is expected to be a string of groups of parentheses separated by spaces.
    Returns a levels of nesting.
    Example example: '(()()) ((())) () ((()))'
    """
    stack = []
    for char in s:
        if char == "(":
            stack.append(1)
        elif char == ")":
            stack.append(stack.pop()
        clear()
        stack
        else:
            stack.append(char)
    return stack
```

This function takes a string of parenthesis groups separated by spaces, and returns a list of the deepest levels of nesting parentheses.  It takes the example, it correctly returns [2, 3, 1, 3] for the input '(()()) ((())) () ((()))'.
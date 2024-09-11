```python
from typing import List
from collections import deque

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of grouped parentheses as input and returns a list of the deepest level of nesting of parentheses for each group.

    Args:
    paren_string (str): A string of grouped parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        stack = deque()
        max_level = 0

        for char in group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                    max_level = max(max_level, stack.__len__() + 1)

        # Add the last level of nesting to max_level
        max_level = max(max_level, stack.__len__() + 1)

        result.append(max_level)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of grouped parentheses as input and returns a list of the deepest level of nesting of parentheses for each group. The function uses a stack to keep track of the nesting level and calculates the maximum level of nesting for each group. Finally, it returns a list of the maximum nesting levels for each group.
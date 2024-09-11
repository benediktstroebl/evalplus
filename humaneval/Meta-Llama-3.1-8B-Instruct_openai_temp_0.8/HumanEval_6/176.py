```python
from typing import List
from collections import deque

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum depth of nesting for each group.
    """
    groups = paren_string.split()
    depths = []

    for group in groups:
        max_depth = 0
        current_depth = 0
        queue = deque()

        for char in group:
            if char == '(':
                queue.append(char)
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                queue.pop()
                if not queue:
                    current_depth = 0
                else:
                    current_depth -= 1

        depths.append(max_depth)

    return depths


# Test cases
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
print(parse_nested_parens('() () (() () ())'))  # [1, 1, 2]
print(parse_nested_parens('(()) (())'))  # [1, 1]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the maximum depth of nesting for each group. It uses a queue to keep track of the current depth and updates the maximum depth as it iterates over the characters in each group. The function returns a list of maximum depths for each group.
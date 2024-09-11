```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string: A string containing multiple groups of parentheses separated by spaces.

    Returns:
        A list of integers representing the maximum level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(group: str) -> int:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth for each group
    groups = paren_string.split()
    result = [max_depth(group) for group in groups]
    return result
```

This script defines a function `max_depth` to calculate the maximum depth of nesting for a single group of parentheses. It then splits the input string into groups and applies the `max_depth` function to each group to get the maximum level of nesting. The results are returned as a list.
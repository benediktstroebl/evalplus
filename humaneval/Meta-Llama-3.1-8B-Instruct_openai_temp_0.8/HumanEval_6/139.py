Here's a Python script that solves the problem:

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest levels of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def calculate_depth(s: str) -> int:
        """ Helper function to calculate the deepest level of nesting of parentheses in a string. """
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the depth of each group
    groups = paren_string.split()
    depths = [calculate_depth(group) for group in groups]

    return depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `calculate_depth` that calculates the deepest level of nesting of parentheses in a given string. It then uses this helper function to split the input string into groups, calculate the depth of each group, and return the list of depths.
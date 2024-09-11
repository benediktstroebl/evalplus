```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string representing multiple groups of nested parentheses and determine the deepest level of nesting for each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers, where each integer represents the deepest level of nesting for the corresponding group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def max_depth(s: str) -> int:
        """Calculate the maximum depth of nesting for a given string of parentheses."""
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth of nesting for each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, we define a helper function `max_depth` to calculate the maximum depth of nesting for a given string of parentheses. The `parse_nested_parens` function then uses this helper function to split the input string into groups and calculate the maximum depth of nesting for each group. The results are returned as a list of integers.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups for nested parentheses separated by spaces.
    For each group, it outputs the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of multiple groups for nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.
    """

    def max_depth(s: str) -> int:
        """Helper function to calculate the maximum depth of a string with nested parentheses."""
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `max_depth` to calculate the maximum depth of parentheses in each group. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth for each group using `max_depth`, and returns the results as a list.
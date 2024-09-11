```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """

    def max_depth(s: str) -> int:
        """Calculate the maximum depth of a string of nested parentheses."""
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth of each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `max_depth` to calculate the maximum depth of a string of nested parentheses. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth of each group using `max_depth`, and returns a list of these values.
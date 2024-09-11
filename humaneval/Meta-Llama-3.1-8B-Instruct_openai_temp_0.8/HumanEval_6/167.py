```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses, separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group of parentheses.
    """
    # Split the input string into groups
    groups = paren_string.split()

    def max_depth(group: str) -> int:
        """
        Calculate the maximum depth of nesting of parentheses in a group.

        Args:
            group (str): A string of nested parentheses.

        Returns:
            int: The maximum depth of nesting.
        """
        depth = 0
        max_depth_so_far = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth_so_far = max(max_depth_so_far, depth)
            elif char == ')':
                depth -= 1
        return max_depth_so_far

    # Calculate the maximum depth of nesting for each group
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string representing multiple groups of nested parentheses as input, and returns a list of the deepest levels of nesting for each group. The `max_depth` function is a helper function that calculates the maximum depth of nesting for a single group of parentheses. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth for each group using `max_depth`, and returns the list of maximum depths.
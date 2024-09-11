```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups separated by spaces containing nested parentheses.

    Returns:
        List[int]: A list of deepest levels of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """ Helper function to find the maximum depth of nesting in a string of parentheses. """
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups and calculate the maximum depth of nesting for each group
    return [max_depth(group) for group in paren_string.split()]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `max_depth` to calculate the maximum depth of nesting in a string of parentheses. It then uses this helper function in the `parse_nested_parens` function to split the input string into groups, calculate the maximum depth of nesting for each group, and return the results as a list.
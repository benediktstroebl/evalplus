```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group in the input string.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """Helper function to calculate the maximum depth of nesting for a given string."""
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into individual groups
    groups = paren_string.split()

    # Calculate the maximum depth for each group and return the result
    return [max_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the maximum depth of nesting for each group. The function uses a helper function `max_depth` to calculate the maximum depth of nesting for a given string. The input string is split into individual groups using the `split` method, and then the maximum depth for each group is calculated using a list comprehension.
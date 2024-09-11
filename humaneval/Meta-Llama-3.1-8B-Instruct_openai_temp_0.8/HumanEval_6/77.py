```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """
        Calculate the maximum depth of nesting for a given string of parentheses.

        Args:
            s (str): A string of parentheses.

        Returns:
            int: The maximum depth of nesting.
        """
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    # Calculate the maximum depth for each group
    depths = [max_depth(group) for group in groups]
    return depths


# Test the function
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that calculates the maximum depth of nesting for each group of parentheses in the input string. The function `max_depth` is a helper function that calculates the maximum depth for a given string of parentheses. The script then tests the `parse_nested_parens` function with the example input string.
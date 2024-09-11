```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting for each group of parentheses in the input string.

    Args:
        paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """Calculate the maximum depth of a string of parentheses."""
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError("Unbalanced parentheses in: " + s)
        if depth!= 0:
            raise ValueError("Unbalanced parentheses in: " + s)
        return max_depth

    # Split the input string into groups and calculate the max depth for each
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a nested function `max_depth` to calculate the maximum depth of a string of parentheses. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth for each group using `max_depth`, and returns the list of depths.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of parenthesized groups separated by spaces, 
    and returns a list of the deepest levels of nesting for each group.

    Args:
    paren_string (str): A string of parenthesized groups separated by spaces.

    Returns:
    List[int]: A list of the deepest levels of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def calculate_max_depth(group: str) -> int:
        """ Helper function to calculate the maximum depth of nesting for a group """
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()

    # Calculate the maximum depth for each group and return the results
    return [calculate_max_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of parenthesized groups separated by spaces and returns a list of the deepest levels of nesting for each group. It uses a helper function `calculate_max_depth` to calculate the maximum depth of nesting for a single group.
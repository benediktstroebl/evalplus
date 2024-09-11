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

    def max_nesting_depth(group: str) -> int:
        # Initialize the maximum depth and the current depth
        max_depth = 0
        current_depth = 0

        # Iterate through each character in the group
        for char in group:
            # If the character is an open parenthesis, increment the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            # If the character is a close parenthesis, decrement the current depth
            elif char == ')':
                current_depth -= 1

        return max_depth

    # Split the input string into groups
    groups = paren_string.split()
    # Initialize an empty list to store the maximum depths
    max_depths = []
    # Iterate through each group and calculate its maximum depth
    for group in groups:
        max_depths.append(max_nesting_depth(group))

    return max_depths
```

This script uses a helper function `max_nesting_depth` to calculate the maximum depth of nesting for each group. It keeps track of the current depth and updates the maximum depth whenever it encounters a deeper level of nesting. The main function splits the input string into groups, calculates the maximum depth for each group using the helper function, and returns a list of maximum depths.
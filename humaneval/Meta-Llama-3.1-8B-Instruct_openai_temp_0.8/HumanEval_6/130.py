```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers where each integer represents the deepest level of nesting of parentheses in each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string into groups based on spaces
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting levels
    max_nesting_levels = []

    # Iterate over each group
    for group in groups:
        # Initialize counters for opening and closing parentheses
        open_paren = 0
        close_paren = 0

        # Initialize the maximum nesting level for the current group
        max_nesting = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the counter
            if char == '(':
                open_paren += 1
                # Update the maximum nesting level if necessary
                max_nesting = max(max_nesting, open_paren - close_paren)
            # If the character is a closing parenthesis, increment the counter
            elif char == ')':
                close_paren += 1

        # Append the maximum nesting level for the current group to the list
        max_nesting_levels.append(max_nesting)

    # Return the list of maximum nesting levels
    return max_nesting_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups based on spaces, and then iterates over each group to find the maximum nesting level. The function returns a list of maximum nesting levels for each group. The script also includes a test case to demonstrate the function's usage.
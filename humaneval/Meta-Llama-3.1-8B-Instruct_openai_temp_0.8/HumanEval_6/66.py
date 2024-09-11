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
    List[int]: A list of deepest level of nesting for each group of parentheses.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the deepest levels of nesting
    deepest_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Use regular expression to find the maximum depth of nested parentheses
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                max_depth = max(max_depth, current_depth)

        # Append the deepest level of nesting to the list
        deepest_levels.append(max_depth)

    return deepest_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a regular approach to find the deepest level of nesting in each group of parentheses. It iterates over each character in the group, incrementing the current depth when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. The maximum depth encountered during the iteration is recorded as the deepest level of nesting for that group.
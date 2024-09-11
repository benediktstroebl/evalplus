```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses in a given string.

    Args:
    paren_string (str): A string consisting of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group of parentheses.
    """

    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Initialize an empty list to store the maximum depth of nesting for each group
    max_depths = []

    # Iterate over each group of parentheses
    for group in paren_groups:
        # Initialize variables to keep track of the current depth and maximum depth
        curr_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                curr_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, curr_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                curr_depth -= 1

        # Append the maximum depth of the current group to the list of maximum depths
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines the `parse_nested_parens` function, which splits the input string into groups of parentheses, iterates over each group, and calculates the maximum depth of nesting by tracking the current depth and updating the maximum depth as needed. The function returns a list of integers representing the maximum depth of nesting for each group of parentheses.
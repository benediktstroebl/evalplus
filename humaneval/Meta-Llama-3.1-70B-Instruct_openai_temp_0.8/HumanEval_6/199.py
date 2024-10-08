```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses in the input string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group of parentheses.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum depth of nesting for each group
    max_depths = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize variables to keep track of the current depth and maximum depth
        current_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                current_depth -= 1

        # Append the maximum depth for the current group to the list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that calculates the maximum depth of nesting for each group of parentheses in the input string. It does this by iterating over each group, keeping track of the current depth and maximum depth, and updating the maximum depth as it encounters opening and closing parentheses. The function returns a list of maximum depths, one for each group of parentheses.
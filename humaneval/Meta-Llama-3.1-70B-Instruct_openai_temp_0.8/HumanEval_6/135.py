```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses in a given string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum depth of nesting for each group
    max_depths = []

    # Iterate over each group
    for group in groups:
        # Initialize the current depth and maximum depth to 0
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

        # Append the maximum depth of the current group to the list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of parentheses separated by spaces as input. It splits the string into groups, then iterates over each group, keeping track of the current depth of nesting and the maximum depth seen so far. The maximum depth for each group is added to a list, which is returned at the end. The script includes a test case to demonstrate its usage.
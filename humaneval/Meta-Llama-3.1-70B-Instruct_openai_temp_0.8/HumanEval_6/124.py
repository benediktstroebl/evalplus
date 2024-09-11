```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it returns the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers where each integer represents the maximum depth of nesting for each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum depths
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

        # Append the maximum depth to the list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines the `parse_nested_parens` function, which takes a string of parentheses groups as input and returns a list of integers representing the maximum depth of nesting for each group. The function splits the input string into groups, then iterates over each group, tracking the current depth and maximum depth of nesting. The maximum depths are stored in a list, which is returned at the end. The script includes an example usage of the function, demonstrating its output for a given input string.
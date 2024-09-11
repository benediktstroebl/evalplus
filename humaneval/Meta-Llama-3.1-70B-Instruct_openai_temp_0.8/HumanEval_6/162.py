```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of space-separated groups of nested parentheses
    and returns a list of the maximum nesting depth for each group.

    Args:
        paren_string (str): The input string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of the maximum nesting depth for each group.
    """

    # Split the input string into separate groups
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting depths
    max_depths = []

    # Iterate over each group
    for group in groups:
        # Initialize the current depth and maximum depth for this group
        curr_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                curr_depth += 1
                # Update the maximum depth if necessary
                max_depth = max(max_depth, curr_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                curr_depth -= 1

        # Append the maximum depth for this group to the list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of space-separated groups of nested parentheses, splits the string into individual groups, and then iterates over each group to calculate the maximum nesting depth. The function returns a list of the maximum nesting depths for each group. The example usage demonstrates the function's behavior with the provided test case.
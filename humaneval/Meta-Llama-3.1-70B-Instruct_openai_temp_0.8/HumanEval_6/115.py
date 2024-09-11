```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses in a given string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter to keep track of the current depth
        depth = 0
        # Initialize a variable to store the maximum depth
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the depth
            if char == '(':
                depth += 1
                # Update the maximum depth if necessary
                max_depth = max(max_depth, depth)
            # If the character is a closing parenthesis, decrement the depth
            elif char == ')':
                depth -= 1

        # Append the maximum depth for the current group to the results list
        results.append(max_depth)

    # Return the list of maximum depths
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines the `parse_nested_parens` function, which takes a string of parentheses groups as input and returns a list of integers representing the maximum depth of nesting for each group. It iterates over each group, keeping track of the current depth and updating the maximum depth as necessary. The results are then returned as a list.
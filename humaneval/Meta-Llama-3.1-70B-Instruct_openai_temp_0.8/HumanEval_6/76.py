```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    # Split the input string into separate groups of parentheses
    groups = paren_string.split()

    # Initialize a list to store the maximum nesting levels for each group
    max_nesting_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize variables to keep track of the current and maximum nesting levels
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                current_level += 1
                # Update the maximum level if the current level is greater
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                current_level -= 1

        # Append the maximum nesting level for the current group to the result list
        max_nesting_levels.append(max_level)

    # Return the list of maximum nesting levels
    return max_nesting_levels


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the maximum nesting level for each group. It uses a simple iterative approach to keep track of the current and maximum nesting levels for each group. The function returns a list of integers representing the maximum nesting levels for each group. The example usage demonstrates how to use the function with a sample input string.
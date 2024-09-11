```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting levels
    max_levels = []

    # Iterate over each group of parentheses
    for group in paren_groups:
        # Initialize variables to keep track of the current and maximum nesting levels
        curr_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                curr_level += 1
                # Update the maximum level if the current level is greater
                max_level = max(max_level, curr_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                curr_level -= 1

        # Append the maximum level for the current group to the result list
        max_levels.append(max_level)

    # Return the list of maximum nesting levels
    return max_levels


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
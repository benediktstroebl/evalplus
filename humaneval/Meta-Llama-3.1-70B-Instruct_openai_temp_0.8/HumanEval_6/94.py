```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of parentheses groups separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum nesting level for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting levels
    max_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current level and the maximum level to 0
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

        # Append the maximum level for the current group to the list
        max_levels.append(max_level)

    # Return the list of maximum nesting levels
    return max_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
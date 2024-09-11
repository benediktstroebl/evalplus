```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    Args:
        paren_string (str): A string of parentheses groups separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting in each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    # Initialize an empty list to store the maximum depth of each group
    max_depths = []

    # Split the input string into groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize variables to keep track of the current depth and the maximum depth
        current_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrease the current depth
            elif char == ')':
                current_depth -= 1

        # Append the maximum depth of the current group to the list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
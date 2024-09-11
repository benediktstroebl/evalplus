```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses groups separated by spaces
    and returns a list of the deepest level of nesting for each group.

    Args:
        paren_string (str): A string of nested parentheses groups separated by spaces

    Returns:
        List[int]: A list of the deepest level of nesting for each group

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    # Initialize an empty list to store the maximum nesting levels
    max_nesting_levels = []

    # Split the input string into individual groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the nesting level
        stack = 0
        # Initialize the maximum nesting level for the current group to 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it to the stack
            if char == '(':
                stack += 1
                # Update the maximum nesting level if necessary
                max_level = max(max_level, stack)
            # If the character is a closing parenthesis, pop the stack
            elif char == ')':
                stack -= 1

        # Append the maximum nesting level for the current group to the list
        max_nesting_levels.append(max_level)

    # Return the list of maximum nesting levels
    return max_nesting_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses groups separated by spaces as input, and returns a list of the deepest level of nesting for each group. The function works by iterating over each group, keeping track of the nesting level using a stack, and updating the maximum nesting level as necessary. The maximum nesting levels for each group are then appended to a list and returned.
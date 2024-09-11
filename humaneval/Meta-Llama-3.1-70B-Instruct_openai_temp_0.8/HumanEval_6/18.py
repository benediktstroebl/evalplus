```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting of parentheses for each group.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the deepest level of nesting for each group
    deepest_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current level of nesting and the deepest level of nesting to 0
        current_level = 0
        deepest_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level of nesting
            if char == '(':
                current_level += 1
                # Update the deepest level of nesting if the current level is greater
                deepest_level = max(deepest_level, current_level)
            # If the character is a closing parenthesis, decrement the current level of nesting
            elif char == ')':
                current_level -= 1

        # Append the deepest level of nesting for the current group to the list
        deepest_levels.append(deepest_level)

    # Return the list of deepest levels of nesting for all groups
    return deepest_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
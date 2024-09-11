### Python Script to Parse Nested Parentheses
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()  # Split the input string into groups
    levels = []  # Initialize an empty list to store the deepest levels

    for group in groups:
        level = 0  # Initialize the current level to 0
        max_level = 0  # Initialize the maximum level to 0

        for char in group:  # Iterate over each character in the group
            if char == '(':  # If the character is an opening parenthesis
                level += 1  # Increase the current level
                max_level = max(max_level, level)  # Update the maximum level
            elif char == ')':  # If the character is a closing parenthesis
                level -= 1  # Decrease the current level

        levels.append(max_level)  # Append the maximum level to the list

    return levels  # Return the list of maximum levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses. The function works by iterating over each group of parentheses, keeping track of the current level of nesting, and updating the maximum level whenever it encounters a higher level. The maximum levels for all groups are then returned as a list.
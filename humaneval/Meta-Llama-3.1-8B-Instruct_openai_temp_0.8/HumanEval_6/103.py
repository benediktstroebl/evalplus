```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
        paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split()

    def nested_level(group: str) -> int:
        # Initialize the maximum level and the current level
        max_level = 0
        current_level = 0

        # Iterate over the characters in the group
        for char in group:
            if char == '(':
                # If the character is an open parenthesis, increment the current level
                current_level += 1
                # Update the maximum level if necessary
                max_level = max(max_level, current_level)
            elif char == ')':
                # If the character is a close parenthesis, decrement the current level
                current_level -= 1

        # Return the maximum level
        return max_level

    # Use a list comprehension to calculate the nested level for each group
    return [nested_level(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of parentheses as input and returns a list of the deepest level of nesting for each group. The function uses a helper function `nested_level` to calculate the nested level for each group. The `nested_level` function iterates over the characters in the group, keeping track of the current level of nesting and updating the maximum level as necessary. The final result is obtained by applying the `nested_level` function to each group using a list comprehension.
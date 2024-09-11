```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of the deepest level of nesting 
    for each group.

    Args:
        paren_string (str): A string containing multiple groups of nested 
                             parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    result = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize variables to keep track of the current level and the max level
        current_level = 0
        max_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                current_level += 1
                # Update the max level if the current level is greater
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                current_level -= 1

        # Append the max level for the group to the result list
        result.append(max_level)

    # Return the result list
    return result

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces, and returns a list of the deepest level of nesting for each group. The function iterates over each group, keeping track of the current level of nesting and the maximum level encountered so far. The maximum level for each group is then appended to the result list, which is returned at the end.
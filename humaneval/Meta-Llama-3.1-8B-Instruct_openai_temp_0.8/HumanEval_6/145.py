```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers, where each integer represents the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Initialize the maximum depth and the current depth to 0
        max_depth = 0
        current_depth = 0

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

        # Append the maximum depth of the current group to the results list
        results.append(max_depth)

    # Return the list of results
    return results

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and then for each group, it iterates over the characters, keeping track of the maximum depth of nesting. The function returns a list of integers, where each integer represents the maximum depth of nesting for each group. The script includes example usage and docstrings for clarity.
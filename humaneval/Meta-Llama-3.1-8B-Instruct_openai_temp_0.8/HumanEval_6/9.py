```python
from typing import List

def calculate_depth(s):
    """Helper function to calculate the maximum depth of nested parentheses in a string."""
    max_depth = depth = 0
    for char in s:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1
    return max_depth

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of maximum depths for each group of nested parentheses.
    """
    # Split the input string into groups
    groups = paren_string.split()
    
    # Calculate the maximum depth for each group
    depths = [calculate_depth(group) for group in groups]
    
    return depths

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
This script first defines a helper function `calculate_depth` to calculate the maximum depth of nested parentheses in a string. It then defines the main function `parse_nested_parens` to split the input string into groups, calculate the maximum depth for each group using the helper function, and return the list of maximum depths. The example usage demonstrates how to use the `parse_nested_parens` function.
```python
from typing import List

def calculate_depth(parens: str) -> int:
    """ Recursively calculates the maximum depth of nesting for a string of parentheses """
    depth = 0
    for char in parens:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0:
                raise ValueError("Unbalanced parentheses")
    if depth!= 0:
        raise ValueError("Unbalanced parentheses")
    return depth

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): Input string containing groups of parentheses separated by spaces

    Returns:
        List[int]: A list of maximum depths for each group of parentheses
    """
    groups = paren_string.split()
    depths = []
    for group in groups:
        try:
            depth = calculate_depth(group)
            depths.append(depth)
        except ValueError as e:
            print(f"Error in group '{group}': {e}")
    return depths

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `calculate_depth` to calculate the maximum depth of nesting for a given string of parentheses. It then defines the `parse_nested_parens` function to split the input string into groups, calculate the depth for each group, and return a list of depths. If a group contains unbalanced parentheses, the script raises a `ValueError` with an error message.
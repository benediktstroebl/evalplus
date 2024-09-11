```python
from typing import List

def calculate_depth(s: str) -> int:
    """
    Helper function to calculate the depth of nesting of parentheses in a string.

    Args:
    s (str): The input string.

    Returns:
    int: The maximum depth of nesting of parentheses.
    """
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    return max_depth


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested 
    parentheses separated by spaces. For each of the group, output the deepest 
    level of nesting of parentheses.

    Args:
    paren_string (str): The input string.

    Returns:
    List[int]: A list of maximum depths of nesting of parentheses for each group.
    """
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Calculate the maximum depth of nesting for the group
        depth = calculate_depth(group)
        # Append the result to the list
        results.append(depth)
    
    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `calculate_depth` to calculate the maximum depth of nesting for each group of parentheses. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth of nesting for each group, and returns a list of these depths.
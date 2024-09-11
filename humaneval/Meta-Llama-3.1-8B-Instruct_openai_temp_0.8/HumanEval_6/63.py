```python
from typing import List

def calculate_depth(paren_string: str) -> int:
    """
    Calculate the maximum depth of nested parentheses in a string.

    Args:
    paren_string (str): A string of parentheses.

    Returns:
    int: The maximum depth of nested parentheses.
    """
    depth = 0
    max_depth = 0
    for char in paren_string:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1
    return max_depth

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of nested parentheses groups separated by spaces.

    Args:
    paren_string (str): A string of nested parentheses groups separated by spaces.

    Returns:
    List[int]: A list of maximum depths of nested parentheses for each group.
    """
    # Split the input string into groups
    groups = paren_string.split()
    
    # Calculate the maximum depth for each group and return the list
    return [calculate_depth(group) for group in groups]

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

In this script, the `calculate_depth` function calculates the maximum depth of nested parentheses in a given string. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth for each group using `calculate_depth`, and returns the list of maximum depths.
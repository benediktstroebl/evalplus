```python
from typing import List

def calculate_depth(s: str) -> int:
    """
    Calculate the maximum depth of nested parentheses in a string.

    Args:
    s (str): A string containing nested parentheses.

    Returns:
    int: The maximum depth of nested parentheses.
    """
    depth = 0
    max_depth = 0
    for char in s:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1
            if depth < 0:
                depth = 0  # Discard negative depth values
    return max_depth


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing multiple groups of nested parentheses to find the maximum depth of nesting in each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum depths of nesting for each group.
    """
    groups = paren_string.split()
    return [calculate_depth(group) for group in groups]


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines two functions: `calculate_depth` and `parse_nested_parens`. The `calculate_depth` function calculates the maximum depth of nested parentheses in a given string. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth of each group using `calculate_depth`, and returns the result as a list.
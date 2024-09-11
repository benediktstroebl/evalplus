```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    groups = paren_string.split()
    max_depths = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        max_depths.append(max_depth)

    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
This script defines the `parse_nested_parens` function, which takes a string of nested parentheses groups as input, splits the string into individual groups, and then calculates the maximum depth of nesting for each group. The function returns a list of integers representing the maximum depth of nesting for each group. The example usage demonstrates how to use the function with a sample input string.
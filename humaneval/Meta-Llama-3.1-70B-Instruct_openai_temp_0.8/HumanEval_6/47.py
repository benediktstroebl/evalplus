```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function parses a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers, where each integer represents the deepest level of nesting for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers, where each integer represents the deepest level of nesting for each group.
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

This script defines the `parse_nested_parens` function, which splits the input string into groups, then iterates over each group to calculate the maximum depth of nesting. The function returns a list of integers, where each integer represents the maximum depth for each group. The example usage demonstrates how to use the function with the provided test case.
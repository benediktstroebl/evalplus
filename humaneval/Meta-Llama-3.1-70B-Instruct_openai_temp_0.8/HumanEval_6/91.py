```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of nested parentheses groups separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum depth of each group.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        result.append(max_depth)

    return result


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script uses a simple stack-based approach to calculate the maximum depth of each group of nested parentheses. It splits the input string into groups, then iterates over each character in each group, updating the current and maximum depths accordingly. The result is a list of integers representing the maximum depth of each group.
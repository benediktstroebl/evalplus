```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()
    max_depths = []

    for group in groups:
        max_depth = 0
        curr_depth = 0

        for char in group:
            if char == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif char == ')':
                curr_depth -= 1

        max_depths.append(max_depth)

    return max_depths

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
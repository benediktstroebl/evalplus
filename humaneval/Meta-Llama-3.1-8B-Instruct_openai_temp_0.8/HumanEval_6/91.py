```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses groups separated by spaces as input.
    For each group, it finds the deepest level of nesting and returns a list of these levels.

    Args:
        paren_string (str): A string of nested parentheses groups separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """
    def calculate_depth(s: str) -> int:
        """Calculates the deepest level of nesting in a string of parentheses."""
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups and calculate the depth for each group
    groups = paren_string.split()
    return [calculate_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses groups as input. It uses a helper function `calculate_depth` to find the deepest level of nesting in each group. The main function splits the input string into groups, calculates the depth for each group, and returns a list of these depths. The script includes a test case to demonstrate the function's behavior.
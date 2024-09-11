```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function parses a string representing multiple groups of nested parentheses
    and returns a list of the deepest level of nesting for each group.

    Args:
        paren_string (str): A string representing multiple groups of nested parentheses
                             separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_nested_parens(group: str) -> int:
        """ Helper function to calculate the deepest level of nesting for a group. """
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups and calculate the deepest level of nesting for each group
    groups = paren_string.split()
    return [max_nested_parens(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that calculates the deepest level of nesting for each group of nested parentheses in the input string. The function uses a helper function `max_nested_parens` to calculate the deepest level of nesting for a single group. The script then tests the function with the example provided in the problem statement.
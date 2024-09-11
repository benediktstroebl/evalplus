```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of multiple groups of nested parentheses separated by spaces.
    For each group, return the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def deepest_nesting(group: str) -> int:
        """Calculate the deepest nesting level of a single group of parentheses."""
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()

    # Calculate the deepest nesting level for each group
    return [deepest_nesting(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```
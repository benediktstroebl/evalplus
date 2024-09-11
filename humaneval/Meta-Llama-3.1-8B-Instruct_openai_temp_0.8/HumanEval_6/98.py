```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum nesting levels for each group in the input string.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting(group: str) -> int:
        """Calculate the maximum nesting level for a group of parentheses."""
        max_level = nesting_level = 0
        for char in group:
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            elif char == ')':
                nesting_level -= 1
        return max_level

    # Split the input string into groups and map the max nesting level for each group
    return list(map(max_nesting, paren_string.split()))

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script defines a function `parse_nested_parens` that calculates the maximum nesting level for each group of nested parentheses in the input string. The function uses a helper function `max_nesting` to calculate the maximum nesting level for a single group. The `parse_nested_parens` function splits the input string into groups, maps the `max_nesting` function to each group, and returns the list of maximum nesting levels. The script includes a test case to demonstrate the function's behavior.
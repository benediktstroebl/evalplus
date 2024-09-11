```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split()

    def calculate_nesting(group: str) -> int:
        """
        Calculate the deepest level of nesting for a given group.

        Args:
        group (str): A string containing nested parentheses.

        Returns:
        int: The deepest level of nesting.
        """
        max_level = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    # Calculate and return the deepest level of nesting for each group
    return [calculate_nesting(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input and returns a list of the deepest levels of nesting for each group. The function splits the input string into groups, calculates the deepest level of nesting for each group using a helper function `calculate_nesting`, and returns the results as a list. The script includes a test case to demonstrate the function's usage.
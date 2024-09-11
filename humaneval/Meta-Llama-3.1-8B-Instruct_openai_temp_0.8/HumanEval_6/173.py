```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def calculate_nesting(group: str) -> int:
        """
        Calculate the deepest level of nesting of parentheses for a given group.

        Args:
        group (str): A string representing a group of nested parentheses.

        Returns:
        int: The deepest level of nesting of parentheses for the given group.
        """
        level = 0
        nesting = 0
        for char in group:
            if char == '(':
                level += 1
                nesting = max(nesting, level)
            elif char == ')':
                level -= 1
        return nesting

    # Split the input string into groups and calculate the deepest level of nesting for each group
    groups = paren_string.split()
    return [calculate_nesting(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups separated by spaces as input. It splits the string into groups, calculates the deepest level of nesting for each group using a helper function `calculate_nesting`, and returns a list of integers representing the deepest level of nesting for each group. The script also includes a test case at the end to demonstrate the function's behavior.
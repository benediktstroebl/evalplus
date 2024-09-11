```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses separated by spaces,
    and outputs the deepest level of nesting of parentheses for each group.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    def max_nesting_level(s: str) -> int:
        """ Helper function to calculate the max nesting level of a single group of parentheses. """
        max_level = 0
        current_level = 0
        for char in s:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    # Split the input string into groups of parentheses
    groups = paren_string.split()
    # Calculate the max nesting level for each group and return as a list
    return [max_nesting_level(group) for group in groups]


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses separated by spaces and returns the deepest level of nesting of parentheses for each group. The function uses a helper function `max_nesting_level` to calculate the max nesting level of a single group of parentheses. The script then splits the input string into groups, calculates the max nesting level for each group, and returns the results as a list. The example usage demonstrates how to use the function.
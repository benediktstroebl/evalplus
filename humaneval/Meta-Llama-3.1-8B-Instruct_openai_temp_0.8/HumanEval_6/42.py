```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers, where each integer represents the deepest level of nesting for its corresponding group.

    Examples:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def max_depth(parens: str) -> int:
        """ Helper function to calculate the maximum depth of nested parentheses. """
        max_depth = 0
        current_depth = 0
        for char in parens:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Split the input string into groups of parentheses and calculate the maximum depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It uses a helper function `max_depth` to calculate the maximum depth of nested parentheses for each group. The main function splits the input string into groups, calculates the maximum depth for each group using the helper function, and returns the results as a list of integers.
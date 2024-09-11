```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers where each integer represents the deepest level of nesting of parentheses for a group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """ Helper function to calculate the maximum depth of nested parentheses. """
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    result = []

    # For each group, calculate the maximum depth of nesting of parentheses
    for group in groups:
        # Remove leading and trailing parentheses if any
        group = group.strip('()')
        result.append(max_depth(group))

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
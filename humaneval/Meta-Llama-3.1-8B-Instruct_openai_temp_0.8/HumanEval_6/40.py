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

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """Function to calculate the maximum depth of nesting of parentheses in a string."""
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Split the input string into groups separated by spaces
    groups = paren_string.split()

    # Calculate the maximum depth of nesting for each group and return the result
    return [max_depth(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and for each group calculates the maximum depth of nesting using a helper function `max_depth`. The result is a list of integers representing the deepest level of nesting of parentheses for each group. The script also includes a test case to demonstrate the function's behavior.
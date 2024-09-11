```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string represented multiple groups for nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest level of nesting of parentheses for each group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    def max_nesting(s: str) -> int:
        # Initialize the maximum nesting level and the current nesting level
        max_level = 0
        curr_level = 0
        for char in s:
            if char == '(':
                # Increase the current nesting level
                curr_level += 1
                # Update the maximum nesting level if necessary
                max_level = max(max_level, curr_level)
            elif char == ')':
                # Decrease the current nesting level
                curr_level -= 1
        return max_level

    # Split the input string by spaces and calculate the maximum nesting level for each group
    return [max_nesting(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of parentheses groups as input, splits the string into groups, and calculates the maximum nesting level of parentheses in each group. The `max_nesting` function is used to calculate the maximum nesting level of parentheses in a single group. The script then tests the function with the example input provided.
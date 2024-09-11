```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_nesting_level(s: str) -> int:
        """ Helper function to calculate the maximum nesting level for a given string. """
        max_level = 0
        current_level = 0
        for char in s:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                if current_level > 0:
                    current_level -= 1
        return max_level

    # Split the input string by spaces and map each group to its maximum nesting level
    return list(map(max_nesting_level, paren_string.split()))


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into individual groups, and returns a list of integers representing the maximum level of nesting for each group. The helper function `max_nesting_level` calculates the maximum nesting level for a given string. The script then tests the function with the provided example input.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses groups separated by spaces
    and returns a list of maximum nesting levels for each group.

    Args:
    paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum nesting levels for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting_level(paren_group: str) -> int:
        """ Helper function to calculate maximum nesting level for a group """
        nesting_level = 0
        max_level = 0
        for char in paren_group:
            if char == '(':
                nesting_level += 1
                max_level = max(max_level, nesting_level)
            elif char == ')':
                nesting_level -= 1
        return max_level

    # Split input string into groups and calculate nesting level for each group
    return [max_nesting_level(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a helper function `max_nesting_level` to calculate the maximum nesting level for each group of parentheses. It iterates over each character in the group, incrementing the nesting level when it encounters an open parenthesis and decrementing when it encounters a close parenthesis. The maximum of the current nesting level and the maximum level seen so far is kept track of and returned at the end.

The main function `parse_nested_parens` splits the input string into groups using the `split` method, applies the `max_nesting_level` function to each group, and returns the list of results.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string with multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(s: str) -> int:
        """Calculate the maximum depth of nesting for a given string."""
        stack = 0
        max_stack = 0
        for c in s:
            if c == '(':
                stack += 1
                max_stack = max(max_stack, stack)
            elif c == ')':
                stack -= 1
        return max_stack

    groups = paren_string.split()
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input. It uses a helper function `max_depth` to calculate the maximum depth of nesting for each group. The `max_depth` function uses a stack to keep track of the current depth of nesting and updates the maximum depth as needed. The main function splits the input string into groups, calculates the maximum depth for each group using `max_depth`, and returns the results as a list.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest level of nesting of parentheses for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(group: str) -> int:
        """Calculate the maximum depth of nesting in a group."""
        stack = 0
        max_stack = 0
        for char in group:
            if char == '(':
                stack += 1
                max_stack = max(max_stack, stack)
            elif char == ')':
                stack -= 1
        return max_stack

    # Split the input string into groups and calculate the maximum depth of nesting for each group
    groups = paren_string.split()
    return [max_depth(group) for group in groups]

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `max_depth` to calculate the maximum depth of nesting in a single group of parentheses. It does this by using a stack to keep track of the current depth of nesting. When it encounters an opening parenthesis, it increments the stack; when it encounters a closing parenthesis, it decrements the stack. The maximum stack size at any point is the maximum depth of nesting in the group.

The main function `parse_nested_parens` then splits the input string into groups using the `split` method, and applies the `max_depth` function to each group to calculate the maximum depth of nesting. The results are returned as a list.
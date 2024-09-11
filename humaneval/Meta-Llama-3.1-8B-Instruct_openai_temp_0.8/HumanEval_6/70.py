```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest level of nesting of parentheses for each group.
    """
    def max_depth(s: str) -> int:
        """Return the maximum depth of a string of nested parentheses."""
        stack = []
        max_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
                max_depth = max(max_depth, len(stack))
            elif c == ')':
                if stack:
                    stack.pop()
        return max_depth

    groups = paren_string.split()
    return [max_depth(g) for g in groups]

# Testing the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines an inner function `max_depth(s)` that calculates the maximum depth of a string of nested parentheses. It then uses this function to calculate the maximum depth of each group in the input string, and returns a list of these maximum depths.
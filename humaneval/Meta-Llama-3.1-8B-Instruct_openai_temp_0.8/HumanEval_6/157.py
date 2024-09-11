```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting of parentheses for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    def count_levels(s: str) -> int:
        """Returns the deepest level of nesting of parentheses in a string."""
        level = 0
        max_level = 0
        for char in s:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        return max_level

    # Split the string into groups and count the levels of each group
    return [count_levels(group) for group in paren_string.split()]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces. It uses a helper function `count_levels` to count the deepest level of nesting of parentheses in each group, and then uses a list comprehension to apply `count_levels` to each group in the input string. The result is a list of the deepest level of nesting of parentheses for each group.
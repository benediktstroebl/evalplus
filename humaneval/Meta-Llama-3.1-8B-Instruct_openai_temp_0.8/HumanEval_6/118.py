```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    levels = []

    for group in groups:
        level = 0
        max_level = 0

        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1

        if level!= 0:
            raise ValueError("Unbalanced parentheses in group: {}".format(group))

        levels.append(max_level)

    return levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It splits the string into groups of parentheses, and for each group, it iterates through the characters to calculate the deepest level of nesting. The function returns a list of deepest levels of nesting for each group. The script includes a test case to demonstrate the function's usage.
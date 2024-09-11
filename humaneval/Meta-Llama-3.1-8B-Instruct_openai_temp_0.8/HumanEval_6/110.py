```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    def deepest_level(s: str) -> int:
        """ Helper function to calculate the deepest level of nesting for a string """
        level = 0
        max_level = 0
        for char in s:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        return max_level

    # Split the input string by spaces and calculate the deepest level for each group
    return [deepest_level(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a recursive helper function `deepest_level` to calculate the deepest level of nesting for a given string of parentheses. It then uses a list comprehension to split the input string by spaces and apply the `deepest_level` function to each group, resulting in a list of the deepest levels of nesting for each group.
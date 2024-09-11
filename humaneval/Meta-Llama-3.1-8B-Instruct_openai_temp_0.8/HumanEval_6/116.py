```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def count_levels(s: str) -> int:
        """ Helper function to count levels of nesting. """
        max_level = 0
        current_level = 0
        for char in s:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    # Split the input string into groups and count levels for each group
    levels = [count_levels(group) for group in paren_string.split()]
    return levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script defines a function `parse_nested_parens` that takes a string of groups of parentheses as input and returns a list of deepest levels of nesting of parentheses for each group. The function uses a helper function `count_levels` to count levels of nesting for each group. The `count_levels` function iterates over the characters in the group, incrementing and decrementing a `current_level` counter as it encounters `(` and `)` characters, respectively. The maximum level encountered is stored in the `max_level` variable, which is returned at the end of the iteration.
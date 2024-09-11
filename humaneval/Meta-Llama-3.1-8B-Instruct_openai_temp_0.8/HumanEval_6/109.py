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
    result = []

    for group in groups:
        depth = 0
        max_depth = 0

        for char in group:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                max_depth = max(max_depth, depth)

        result.append(max_depth)

    return result


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses. The script uses a simple iterative approach to calculate the maximum depth of nesting for each group. The result is then returned as a list.
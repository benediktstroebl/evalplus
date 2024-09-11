```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest levels of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    groups = paren_string.split()

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
            raise ValueError(f"Invalid parentheses group: {group}")
        result.append(max_level)

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input and returns a list of the deepest levels of nesting for each group. It iterates over each group of parentheses, keeping track of the current level of nesting and the maximum level encountered so far. The function handles invalid groups (i.e., groups with unbalanced parentheses) by raising a `ValueError`. The script also includes a test case to demonstrate the function's usage.
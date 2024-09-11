```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    parens_groups = paren_string.split()

    for group in parens_groups:
        depth = 0
        max_depth = 0

        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1

        result.append(max_depth)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by iterating over each group of parentheses, keeping track of the current depth (i.e., the difference between the number of open and close parentheses encountered so far), and updating the maximum depth whenever it finds a group with a greater depth. The maximum depth for each group is then added to the result list.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups of nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        result.append(max_depth)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script splits the input string into groups of nested parentheses, then for each group, it keeps track of the maximum depth of nesting encountered so far. The `max_depth` variable stores the maximum depth encountered, and the `current_depth` variable stores the current depth. The script then appends the maximum depth for each group to the result list.
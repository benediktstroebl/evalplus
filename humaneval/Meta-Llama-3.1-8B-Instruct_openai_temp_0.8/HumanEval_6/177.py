```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest levels of nesting for each group of parentheses.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
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

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input and returns a list of the deepest levels of nesting for each group. The function iterates over each group, keeping track of the current depth of nesting and the maximum depth encountered so far. The maximum depth is updated whenever a closing parenthesis is encountered (since this will decrease the depth by 1, and we want the maximum depth seen so far). The final list of maximum depths is returned.
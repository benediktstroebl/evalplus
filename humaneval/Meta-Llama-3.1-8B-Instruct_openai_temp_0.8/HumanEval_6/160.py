### Nested Parentheses Depth Calculator
#### A Python script to calculate the maximum depth of nested parentheses in a given string.

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the maximum depth of nesting for each group of parentheses.

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

This script splits the input string into groups, then iterates through each character in a group to calculate the maximum depth of nesting. The result is a list of the maximum depth of nesting for each group.
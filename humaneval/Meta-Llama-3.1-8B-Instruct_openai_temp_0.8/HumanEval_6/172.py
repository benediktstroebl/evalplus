```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string of multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    groups = paren_string.split()

    for group in groups:
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


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of parentheses separated by spaces as input. It then iterates over each group, tracking the maximum depth of parentheses seen so far. The maximum depth is calculated by incrementing the depth when an opening parenthesis is encountered and decrementing the depth when a closing parenthesis is encountered. The maximum depth seen for each group is then appended to the result list. Finally, the function returns the result list.
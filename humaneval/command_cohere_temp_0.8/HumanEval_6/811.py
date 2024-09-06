Here's a Python script with a self-contained function that solves the problem using a `depth` counter to track the depth of nesting:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

Returns:
A list of deepest levels of nesting for each group of parentheses
"""
    res: List[int] = []
    nested_levels = 0

    for char in s:
        if char == '(':
            nested_levels += 1
        elif char == ')':
            if nested_levels > 0:
                nested_levels -= 1
            else:
                res.append(nested_levels)
                nested_levels = 0

    return res

# Test Cases
assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
assert parse_nested_parens('()') == [0]
assert parse_nested_parens('(()())') == [2]
assert parse_nested_parens('(((())))') == [3]
```

The function uses a counter `nested_levels` to keep track of the nesting level whenever it encounters an opening parenthesis. When it encounters a closing parenthesis, it checks if the counter is not zero, meaning there's an extra level of nesting to resolve, otherwise, it means the counter reflects the deepest level of nesting in the current group, and thus, it adds the value of the counter to the result list and resets it to zero.
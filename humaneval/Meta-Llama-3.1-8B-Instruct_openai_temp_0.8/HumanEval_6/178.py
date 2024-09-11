```python
from typing import List

def max_depth(s: str) -> int:
    """ Calculate the maximum depth of parentheses in a string. """
    depth = max_depth_helper = 0
    for char in s:
        if char == '(':
            max_depth_helper += 1
            depth = max(depth, max_depth_helper)
        elif char == ')':
            if max_depth_helper > 0:
                max_depth_helper -= 1
    return depth


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses 
    separated by spaces. For each of the group, output the deepest level of nesting of parentheses. """
    groups = paren_string.split()
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `max_depth` to calculate the maximum depth of parentheses in a string. It then defines the main function `parse_nested_parens` to split the input string into groups, calculate the maximum depth of each group, and return the results as a list.
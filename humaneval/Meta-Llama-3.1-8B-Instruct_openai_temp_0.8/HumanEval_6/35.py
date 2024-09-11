```python
from typing import List

def max_depth(s: str) -> int:
    """ Returns the maximum depth of nesting in the given string of parentheses. """
    depth = 0
    max_depth = 0
    for c in s:
        if c == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif c == ')':
            depth -= 1
    return max_depth

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): A string representing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum nesting depths for each group in the input string.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups separated by spaces
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum depths for each group
    depths = []
    
    # Iterate over each group and calculate its maximum depth
    for group in groups:
        depth = max_depth(group)
        depths.append(depth)
    
    return depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script defines two functions: `max_depth` and `parse_nested_parens`. The `max_depth` function calculates the maximum depth of nesting in a given string of parentheses, while the `parse_nested_parens` function splits the input string into groups, calculates the maximum depth for each group, and returns these depths in a list.
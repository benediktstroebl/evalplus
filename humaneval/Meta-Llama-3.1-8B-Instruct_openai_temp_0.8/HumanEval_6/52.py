```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.
    
    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    
    def max_depth(group: str) -> int:
        """Return the maximum depth of nesting in a given group."""
        
        depth = 0
        max_depth = 0
        
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        
        return max_depth
    
    # Split the input string into groups and calculate the maximum depth for each group
    return [max_depth(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that calculates the maximum depth of nesting for each group of parentheses in the input string. The function uses a helper function `max_depth` to calculate the maximum depth for each group. The `max_depth` function iterates through each character in the group, incrementing the depth when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. It keeps track of the maximum depth encountered so far and returns it at the end. The `parse_nested_parens` function splits the input string into groups, calculates the maximum depth for each group using `max_depth`, and returns the list of maximum depths.
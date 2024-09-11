```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Parameters:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of maximum levels of nesting for each group of parentheses.
    
    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    
    def max_depth(s: str) -> int:
        """
        Helper function to calculate the maximum depth of nesting for a given string.
        
        Parameters:
        s (str): A string containing nested parentheses.
        
        Returns:
        int: The maximum level of nesting.
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth
    
    # Split the input string by spaces and calculate the maximum depth for each group
    groups =(paren_string.replace('(', '( ').replace(')',')').split())
    return [max_depth(group) for group in groups]


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It uses a helper function `max_depth` to calculate the maximum depth of nesting for each group of parentheses. The groups are split from the input string using spaces, and the maximum depth is calculated for each group. The result is a list of maximum levels of nesting for each group.
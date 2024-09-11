```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    
    def max_depth(group: str) -> int:
        """
        Helper function to calculate the deepest level of nesting of parentheses in a group.
        
        Args:
        group (str): A string representing a group of nested parentheses.
        
        Returns:
        int: The deepest level of nesting of parentheses in the group.
        """
        max_level = 0
        current_level = 0
        
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                if current_level > 0:
                    current_level -= 1
        
        return max_level
    
    # Split the input string into groups and calculate the maximum depth for each group
    groups = paren_string.split()
    result = [max_depth(group) for group in groups]
    
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses as input. It uses a helper function `max_depth` to calculate the deepest level of nesting of parentheses in each group. The main function then splits the input string into groups, calculates the maximum depth for each group, and returns the result as a list. The script includes a test case to demonstrate the function's usage.
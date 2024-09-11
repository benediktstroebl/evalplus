```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum level of nesting for each group of parentheses in a given string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum level of nesting for each group.

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum level of nesting for each group
    max_nesting = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize counters for open and close parentheses
        open_paren = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, increment the open counter
            if char == '(':
                open_paren += 1
                # Update the maximum level if necessary
                max_level = max(max_level, open_paren)
            # If the character is a close parenthesis, decrement the open counter
            elif char == ')':
                open_paren -= 1
                # Update the maximum level if necessary
                max_level = max(max_level, open_paren)
        
        # Append the maximum level of nesting for the current group to the result list
        max_nesting.append(max_level)
    
    # Return the list of maximum levels of nesting
    return max_nesting

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of parentheses as input, splits it into groups, and calculates the maximum level of nesting for each group. The function returns a list of integers representing the maximum level of nesting for each group. The script includes a test case to demonstrate the function's usage.
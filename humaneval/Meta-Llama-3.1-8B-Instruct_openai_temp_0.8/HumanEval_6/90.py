```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function parses a string of nested parentheses separated by spaces and returns 
    a list of the maximum nesting depth for each group.

    Args:
        paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the maximum nesting depth for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """

    # Split the input string into groups by spaces
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting depth for each group
    max_depths = []

    # Iterate over each group
    for group in groups:
        # Use regular expression to find all the nesting levels in the group
        match = re.finditer(r'\([^()]*\)', group)
        
        # Initialize the maximum depth to 0
        max_depth = 0
        
        # Iterate over the nesting levels
        for match_obj in match:
            # Calculate the depth of the current nesting level
            depth = match_obj.regs[0][1] - match_obj.regs[0][0] + 2
            
            # Update the maximum depth
            max_depth = max(max_depth, depth)
        
        # Append the maximum depth for the current group to the list
        max_depths.append(max_depth)

    # Return the list of maximum nesting depths
    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the maximum nesting depth for each group. It uses regular expressions to find all the nesting levels in each group and keeps track of the maximum depth. The function returns a list of maximum nesting depths for each group. The script includes a test case at the end to demonstrate the function's usage.
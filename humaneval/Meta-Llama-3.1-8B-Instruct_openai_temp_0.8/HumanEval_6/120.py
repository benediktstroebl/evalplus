```python
from typing import List
import re


def parse_nested_parens(paren_string: str) -> List[int]:
    """ 
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    
    # Split the input string into groups
    groups = re.split(r'\s+', paren_string)
    
    # Initialize an empty list to store the maximum depth of each group
    max_depths = []
    
    # Loop over each group
    for group in groups:
        # Initialize variables to keep track of the current depth and maximum depth
        current_depth = 0
        max_depth = 0
        
        # Loop over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                current_depth -= 1
        
        # Append the maximum depth of the group to the list
        max_depths.append(max_depth)
    
    # Return the list of maximum depths
    return max_depths


# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a regular expression to split the input string into groups, then loops over each group to calculate the maximum depth of nested parentheses. The maximum depth is calculated by keeping track of the current depth (i.e., the number of opening parentheses that have not yet been matched with a closing parenthesis) and updating it whenever an opening or closing parenthesis is encountered. The script then appends the maximum depth of each group to a list, which is returned at the end.
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses groups as input.
    It parses each group and returns a list of the maximum level of nesting for each group.

    Args:
        paren_string (str): A string of multiple groups for nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the maximum level of nesting for each group.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum levels of nesting
    max_levels = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current level and the maximum level to 0
        curr_level, max_level = 0, 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current level
            if char == '(':
                curr_level += 1
            # If the character is a closing parenthesis, decrease the current level
            elif char == ')':
                curr_level -= 1
            # Update the maximum level if the current level is greater
            max_level = max(max_level, curr_level)
        
        # Append the maximum level of the current group to the list
        max_levels.append(max_level)
    
    # Return the list of maximum levels
    return max_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script takes a string of multiple groups for nested parentheses as input, parses each group, and returns a list of the maximum level of nesting for each group. The function splits the input string into groups of parentheses, then iterates over each group to find the maximum level of nesting by keeping track of the current level and the maximum level. The maximum levels of all groups are stored in a list and returned as the output.
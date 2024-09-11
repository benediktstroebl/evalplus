```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses as input.
    For each group, it calculates the maximum level of nesting of the parentheses.
    
    Args:
    paren_string (str): A string of groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of integers, where each integer is the maximum level of nesting of the corresponding group of parentheses.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum level of nesting for each group
    max_levels = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter to keep track of the current level of nesting
        level = 0
        # Initialize a flag to indicate whether we are currently inside a group of parentheses
        inside_group = False
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, increment the level and set the flag to True
            if char == '(':
                level += 1
                inside_group = True
            # If the character is a close parenthesis, decrement the level and set the flag to False
            elif char == ')':
                level -= 1
                inside_group = False
                # If the level is negative, reset it to 0 (this can happen if there are mismatched parentheses)
                if level < 0:
                    level = 0
        
        # The maximum level of nesting for the group is the maximum level encountered
        max_levels.append(level)
    
    # Return the list of maximum levels
    return max_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
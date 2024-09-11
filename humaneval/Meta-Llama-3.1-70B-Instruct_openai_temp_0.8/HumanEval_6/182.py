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
    """
    
    # Split the input string into separate groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum nesting levels
    max_nesting_levels = []
    
    # Iterate over each group
    for group in groups:
        # Initialize the current nesting level and the maximum nesting level
        current_level = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                current_level += 1
                # Update the maximum nesting level if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                current_level -= 1
        
        # Append the maximum nesting level for the current group to the list
        max_nesting_levels.append(max_level)
    
    # Return the list of maximum nesting levels
    return max_nesting_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
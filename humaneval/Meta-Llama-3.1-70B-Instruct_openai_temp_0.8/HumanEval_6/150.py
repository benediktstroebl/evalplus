```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum nesting depth of parentheses for each group in the input string.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
        List[int]: A list of integers representing the maximum nesting depth for each group of parentheses.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum nesting depths
    max_depths = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current nesting depth and the maximum nesting depth to 0
        curr_depth = 0
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting depth
            if char == '(':
                curr_depth += 1
                # Update the maximum nesting depth if the current depth is greater
                max_depth = max(max_depth, curr_depth)
            # If the character is a closing parenthesis, decrement the current nesting depth
            elif char == ')':
                curr_depth -= 1
        
        # Append the maximum nesting depth for the current group to the list
        max_depths.append(max_depth)
    
    # Return the list of maximum nesting depths
    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
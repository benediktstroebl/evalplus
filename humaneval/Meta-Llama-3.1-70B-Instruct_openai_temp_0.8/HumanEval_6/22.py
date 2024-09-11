```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of integers representing the maximum level of nesting for each group of parentheses.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    result = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize variables to track the current level of nesting and the maximum level
        current_level = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level of nesting
            if char == '(':
                current_level += 1
                # Update the maximum level if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level of nesting
            elif char == ')':
                current_level -= 1
        
        # Append the maximum level of nesting for the current group to the result list
        result.append(max_level)
    
    return result

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
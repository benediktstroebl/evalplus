```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nesting for each group of parentheses.
    
    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize the current depth and the maximum depth to 0
        current_depth = 0
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current depth
            if char == '(':
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrease the current depth
            elif char == ')':
                current_depth -= 1
        
        # Append the maximum depth of the current group to the results
        results.append(max_depth)
    
    # Return the list of results
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of the deepest level of nesting 
    for each group.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses 
                        separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize the current level and the maximum level to 0
        current_level = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, increase the current level
            if char == '(':
                current_level += 1
                # Update the maximum level if necessary
                max_level = max(max_level, current_level)
            # If the character is a close parenthesis, decrease the current level
            elif char == ')':
                current_level -= 1
        
        # Append the maximum level for this group to the results
        results.append(max_level)
    
    # Return the results
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```
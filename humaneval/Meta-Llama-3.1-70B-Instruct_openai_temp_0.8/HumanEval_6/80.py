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
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum nesting levels
    max_nestings = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize variables to keep track of the current and maximum nesting levels
        curr_nesting = 0
        max_nesting = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current nesting level
            if char == '(':
                curr_nesting += 1
                # Update the maximum nesting level if necessary
                max_nesting = max(max_nesting, curr_nesting)
            # If the character is a closing parenthesis, decrease the current nesting level
            elif char == ')':
                curr_nesting -= 1
        
        # Append the maximum nesting level for this group to the list
        max_nestings.append(max_nesting)
    
    # Return the list of maximum nesting levels
    return max_nestings


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
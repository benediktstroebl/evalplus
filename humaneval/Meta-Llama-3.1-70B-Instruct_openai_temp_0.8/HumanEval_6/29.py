```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of integers representing the 
    deepest level of nesting for each group.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses 
                        separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting 
               for each group.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize a list to store the maximum depth for each group
    max_depths = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the opening parentheses
        stack = []
        
        # Initialize the maximum depth for this group
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth if necessary
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the corresponding 
            # opening parenthesis from the stack
            elif char == ')':
                stack.pop()
        
        # Add the maximum depth for this group to the list
        max_depths.append(max_depth)
    
    # Return the list of maximum depths
    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nested parentheses for each group in the input string.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of maximum depth of nested parentheses for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum depth for each group
    max_depths = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a counter to track the current depth
        current_depth = 0
        # Initialize a counter to track the maximum depth
        max_depth = 0
        
        # Initialize a stack to track the opening parentheses
        stack = []
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack and increment the current depth
            if char == '(':
                stack.append(char)
                current_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and decrement the current depth
            elif char == ')':
                if stack:
                    stack.pop()
                    current_depth -= 1
        
        # Append the maximum depth for the current group to the result list
        max_depths.append(max_depth)
    
    # Return the list of maximum depths
    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script first splits the input string into groups of nested parentheses. Then for each group, it uses a stack to track the opening parentheses and calculates the maximum depth of nested parentheses. The maximum depth for each group is appended to a list, which is finally returned as the result.
Here is a Python script that solves the problem using a stack-based approach.

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group.
    """
    groups = paren_string.split()  # Split the input string into groups of parentheses
    max_depths = []  # Initialize a list to store the maximum depth of each group
    
    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth for the current group
        stack = []  # Initialize a stack to keep track of the opening parentheses
        
        for char in group:
            if char == '(':  # If the character is an opening parenthesis
                stack.append(char)  # Push it onto the stack
                current_depth = len(stack)  # Update the current depth
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis
                stack.pop()  # Pop the corresponding opening parenthesis from the stack
        
        max_depths.append(max_depth)  # Append the maximum depth of the current group to the result list
    
    return max_depths

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script works by iterating over each group of parentheses, using a stack to keep track of the opening parentheses. The maximum depth of each group is updated whenever a new maximum depth is reached. The result is a list of integers representing the maximum depth of nesting for each group.
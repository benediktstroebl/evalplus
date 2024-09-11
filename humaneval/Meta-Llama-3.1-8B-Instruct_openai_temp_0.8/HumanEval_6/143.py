```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses for each group in the input string.

    Args:
    paren_string (str): A string containing multiple groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting of parentheses for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the opening parentheses
        stack = []
        
        # Initialize a variable to store the maximum depth
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it into the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth if the stack size is greater than the current maximum depth
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()
        
        # Append the maximum depth for the current group to the results list
        results.append(max_depth)
    
    # Return the list of results
    return results

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This Python script uses a stack to keep track of the opening parentheses and calculates the deepest level of nesting for each group in the input string. It iterates over each group, pushes opening parentheses into the stack, and updates the maximum depth whenever a new maximum depth is found. Finally, it returns a list of the maximum depths for each group.
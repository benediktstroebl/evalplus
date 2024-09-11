```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses for each group in a given string.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the nesting level
        stack = []
        
        # Initialize the maximum nesting level for the current group
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                stack.pop()
                # Update the maximum nesting level if the stack is not empty
                max_level = max(max_level, len(stack) + 1)
        
        # Add the maximum nesting level for the current group to the results list
        results.append(max_level)
    
    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group. The function uses a stack to keep track of the nesting level and iterates over each character in the input string to update the stack and the maximum nesting level. Finally, it returns a list of maximum nesting levels for each group. The script includes a test case to demonstrate the function's behavior.
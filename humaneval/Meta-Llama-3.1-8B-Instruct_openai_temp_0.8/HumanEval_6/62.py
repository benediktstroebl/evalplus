```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces, 
    and returns a list of the deepest level of nesting for each group.

    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the depth
        stack = []
        # Initialize the maximum depth to 0
        max_depth = 0
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the last opening parenthesis from the stack
            elif char == ')':
                stack.pop()
        # Append the maximum depth for the current group to the results list
        results.append(max_depth)
    
    # Return the list of maximum depths
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group. The function uses a stack to keep track of the depth of the parentheses and iterates over each group to calculate the maximum depth. The results are appended to a list and returned at the end. The script also includes a test case to demonstrate the function's usage.
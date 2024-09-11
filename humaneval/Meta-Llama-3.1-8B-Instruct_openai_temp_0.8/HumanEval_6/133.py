```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of the nesting level
        stack = []
        
        # Initialize the maximum nesting level to 0
        max_nesting = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()
                    # Increase the maximum nesting level if the stack is not empty after popping
                    max_nesting = max(max_nesting, len(stack))
        
        # Append the maximum nesting level for the current group to the results list
        results.append(max_nesting)
    
    # Return the list of maximum nesting levels
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first splits the input string into individual groups of parentheses, then iterates over each group. For each group, it uses a stack to keep track of the nesting level, increasing the maximum nesting level whenever it encounters a closing parenthesis and the stack is not empty. Finally, it appends the maximum nesting level for each group to the results list and returns it.
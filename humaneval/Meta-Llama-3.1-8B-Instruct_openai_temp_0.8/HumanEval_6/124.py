```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of parentheses groups separated by spaces as input.
    It returns a list of integers representing the maximum nesting level of each group.
    
    :param paren_string: A string of groups of parentheses separated by spaces.
    :return: A list of integers representing the maximum nesting level of each group.
    """
    
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum nesting levels
    nesting_levels = []
    
    # Iterate over each group of parentheses
    for group in groups:
        # Initialize counters for open and close parentheses
        open_count = 0
        max_open = 0
        
        # Initialize a stack to keep track of the nesting level
        stack = []
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                open_count += 1
                max_open = max(max_open, open_count)
            # If the character is a close parenthesis, pop the corresponding open parenthesis off the stack
            elif char == ')':
                if stack:
                    stack.pop()
                    open_count -= 1
        
        # Append the maximum nesting level to the list
        nesting_levels.append(max_open)
    
    # Return the list of maximum nesting levels
    return nesting_levels

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of parentheses groups separated by spaces as input and returns a list of integers representing the maximum nesting level of each group. The function uses a stack to keep track of the nesting level and iterates over each group of parentheses to calculate the maximum nesting level. The example usage at the end demonstrates how to use the function with the provided test case.
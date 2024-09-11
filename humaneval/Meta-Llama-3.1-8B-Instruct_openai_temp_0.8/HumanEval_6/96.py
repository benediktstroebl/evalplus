```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    e.g. (()()) has maximum two levels of nesting while ((())) has three.
    
    :param paren_string: A string containing multiple groups of nested parentheses separated by spaces.
    :return: A list of deepest levels of nesting for each group.
    """
    
    # Split the input string into groups by spaces
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a stack to keep track of opening parentheses
        stack = []
        
        # Initialize a variable to store the maximum depth
        max_depth = 0
        
        # Initialize a variable to store the current depth
        current_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it to the stack and increment the current depth
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
        
        # Append the maximum depth of the current group to the result list
        result.append(max_depth)
    
    # Return the result list
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input. It splits the input string into groups separated by spaces, then iterates over each group to calculate the maximum depth of nesting. The maximum depth is calculated by maintaining a stack of opening parentheses and keeping track of the current depth. The script then returns a list of maximum depths for each group.
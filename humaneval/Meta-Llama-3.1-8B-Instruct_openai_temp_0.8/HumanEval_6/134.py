```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function parses a string of nested parentheses and returns a list of the maximum
    depth at which each group of parentheses is nested.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the maximum depth at which each group of parentheses is nested.
    """
    depths = []
    for group in paren_string.split():
        # Initialize the maximum depth and the current depth
        max_depth = 0
        curr_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # If we encounter an open parenthesis, increment the current depth
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif char == ')':
                # If we encounter a close parenthesis, decrement the current depth
                curr_depth -= 1
        
        # Append the maximum depth of the current group to the list of depths
        depths.append(max_depth)
    
    return depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the maximum depth at which each group of parentheses is nested. It does this by iterating over each group of parentheses, incrementing the current depth when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. The maximum depth seen so far is then appended to the list of depths. Finally, the function is tested with the example provided.
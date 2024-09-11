```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses in each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the deepest level of nesting for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the maximum nesting depth for each group
    max_depths = []
    
    # Iterate over each group
    for group in groups:
        # Initialize counters for the current nesting depth and the maximum nesting depth
        current_depth = 0
        max_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting depth
            if char == '(':
                current_depth += 1
                # Update the maximum nesting depth if necessary
                max_depth = max(max_depth, current_depth)
            # If the character is a closing parenthesis, decrement the current nesting depth
            elif char == ')':
                current_depth -= 1
        
        # Add the maximum nesting depth for the current group to the list
        max_depths.append(max_depth)
    
    # Return the list of maximum nesting depths
    return max_depths

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the maximum nesting depth for each group of parentheses. The function iterates over each group, keeping track of the current nesting depth and the maximum nesting depth encountered so far. The maximum nesting depth for each group is then added to the list, which is returned at the end. The function is tested with the example input provided in the problem statement.
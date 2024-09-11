```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it calculates the deepest level of nesting of parentheses.
    
    Args:
        paren_string (str): The input string of groups of nested parentheses.
    
    Returns:
        List[int]: A list of deepest levels of nesting for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current nesting level
        nesting_level = 0
        # Initialize a flag to check if we are currently inside a group
        inside_group = False
        # Initialize a counter to keep track of the deepest nesting level
        max_nesting_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the nesting level and set the flag to True
            if char == '(':
                nesting_level += 1
                inside_group = True
                # Update the max nesting level if necessary
                max_nesting_level = max(max_nesting_level, nesting_level)
            # If the character is a closing parenthesis, decrement the nesting level and set the flag to False
            elif char == ')':
                nesting_level -= 1
                inside_group = False
        
        # If the group was not empty, add the max nesting level to the results
        if inside_group:
            results.append(max_nesting_level + 1)
        else:
            results.append(0)
    
    # Return the list of results
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of groups of nested parentheses and returns a list of the deepest levels of nesting for each group. It uses a simple counter-based approach to keep track of the current nesting level and the max nesting level seen so far. The script also includes a test case to demonstrate the function's correctness.
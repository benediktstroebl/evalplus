```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses groups as input, where each group is separated by a space.
    It returns a list of integers, where each integer represents the maximum level of nesting in the corresponding group.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers, where each integer represents the maximum level of nesting in the corresponding group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize the current level and maximum level to 0
        current_level = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                current_level -= 1
        
        # Append the maximum level to the results list
        results.append(max_level)
    
    # Return the results list
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses groups as input and returns a list of integers representing the maximum level of nesting in each group. It works by iterating over each group, tracking the current level of nesting, and updating the maximum level as necessary. The function is then tested with the provided example input.
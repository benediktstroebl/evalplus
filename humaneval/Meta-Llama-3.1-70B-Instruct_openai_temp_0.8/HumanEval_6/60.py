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
    # Split the input string into groups of parentheses
    paren_groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group of parentheses
    for group in paren_groups:
        # Initialize the current nesting level and the maximum nesting level
        current_level = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                current_level += 1
                # Update the maximum nesting level if necessary
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                current_level -= 1
        
        # Append the maximum nesting level for this group to the results list
        results.append(max_level)
    
    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```

This script works by iterating over each group of parentheses, and for each group, it iterates over each character. It keeps track of the current nesting level and the maximum nesting level seen so far. When it encounters an opening parenthesis, it increments the current nesting level and updates the maximum nesting level if necessary. When it encounters a closing parenthesis, it decrements the current nesting level. Finally, it appends the maximum nesting level for each group to the results list and returns it.
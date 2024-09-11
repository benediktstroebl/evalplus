```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting for each group of parentheses in a given string.
    
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
        # Initialize variables to keep track of the current level and maximum level
        current_level = 0
        max_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                current_level += 1
                # Update the maximum level if the current level is greater
                max_level = max(max_level, current_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                current_level -= 1
        
        # Append the maximum level for the current group to the results list
        results.append(max_level)
    
    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
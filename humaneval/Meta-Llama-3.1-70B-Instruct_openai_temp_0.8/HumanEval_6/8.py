```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses for each group.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current nesting level
        nesting_level = 0
        # Initialize a variable to store the maximum nesting level
        max_nesting_level = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the nesting level
            if char == '(':
                nesting_level += 1
                # Update the maximum nesting level if necessary
                max_nesting_level = max(max_nesting_level, nesting_level)
            # If the character is a closing parenthesis, decrease the nesting level
            elif char == ')':
                nesting_level -= 1
        
        # Append the maximum nesting level for the current group to the results list
        results.append(max_nesting_level)
    
    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
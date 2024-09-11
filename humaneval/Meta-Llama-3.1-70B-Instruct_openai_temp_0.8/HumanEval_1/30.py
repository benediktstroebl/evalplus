```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, where each string represents a separate group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separate groups of parentheses
    paren_groups = []
    
    # Initialize an empty string to build the current group of parentheses
    current_group = ''
    
    # Initialize a counter to keep track of the nesting level of the parentheses
    nesting_level = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group of parentheses
        current_group += char
        
        # If the character is an open parenthesis, increment the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
        elif char == ')':
            nesting_level -= 1
            
            # If the nesting level is zero, it means we've finished a group of parentheses
            if nesting_level == 0:
                # Add the current group of parentheses to the list of groups
                paren_groups.append(current_group)
                # Reset the current group of parentheses
                current_group = ''
    
    # Return the list of separate groups of parentheses
    return paren_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
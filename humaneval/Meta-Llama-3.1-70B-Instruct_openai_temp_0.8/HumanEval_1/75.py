```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string is a group of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize variables to keep track of the current group and the list of groups
    current_group = ''
    groups = []
    
    # Initialize a counter to keep track of the nesting level
    nesting_level = 0
    
    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a closing parenthesis, decrease the nesting level
        elif char == ')':
            nesting_level -= 1
        
        # Add the character to the current group
        current_group += char
        
        # If the nesting level is zero, it means we have a complete group
        if nesting_level == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ''
    
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
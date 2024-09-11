```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Initialize a counter to keep track of the nesting level
    nesting_level = 0
    
    # Iterate over the characters in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char
        
        # If the character is an open parenthesis, increment the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
        elif char == ')':
            nesting_level -= 1
            
            # If the nesting level is zero, it means we've finished a group
            if nesting_level == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group
                current_group = ''
    
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
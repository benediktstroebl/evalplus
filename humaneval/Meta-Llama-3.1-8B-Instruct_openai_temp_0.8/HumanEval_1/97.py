```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate a string containing multiple groups of nested parentheses into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the groups
    groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty substring to build the current group
    group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the group
        if char == '(':
            stack.append(char)
            group += char
        # If the character is a closing parenthesis, pop the opening parenthesis from the stack and add it to the group
        elif char == ')':
            stack.pop()
            group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                groups.append(group)
                group = ''
    
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each representing a separate group of balanced parentheses. The function uses a stack to keep track of the opening parentheses and a substring to build the current group. When a complete group is found, it is added to the list of groups and the process starts over. The function ignores any spaces in the input string and returns the list of groups.
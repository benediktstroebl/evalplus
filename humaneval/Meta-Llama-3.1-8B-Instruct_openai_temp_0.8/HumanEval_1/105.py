```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignoring any spaces in the input string.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a group of balanced nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build each group
    group = ''
    
    # Iterate over the input string
    for i, char in enumerate(paren_string):
        # If the character is an opening parenthesis
        if char == '(':
            # Push it to the stack
            stack.append(char)
            # Add it to the current group
            group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # Pop the opening parenthesis from the stack
            stack.pop()
            # Add the closing parenthesis to the current group
            group += char
            # If the stack is empty, it means we've found a complete group
            if not stack:
                # Add the group to the list of groups
                groups.append(group)
                # Reset the group
                group = ''
    
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that separates the input string into groups of balanced nested parentheses. It uses a stack to keep track of the opening parentheses and a string to build each group. When a complete group is found, it adds the group to the list of groups and resets the string to build the next group. Finally, it returns the list of groups. The script also includes a test case to demonstrate the function's correctness.
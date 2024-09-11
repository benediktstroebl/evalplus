```python
from typing import List
from collections import deque

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates multiple groups of nested parentheses in a given string into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize a stack to keep track of opening parentheses
    stack = deque()
    
    # Initialize a list to store the separated groups
    groups = []
    
    # Initialize the current group
    group = ""
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is empty, it means there's a mismatched closing parenthesis, so ignore it
            if not stack:
                continue
            # Pop the opening parenthesis from the stack and add it to the current group
            stack.pop()
            group += char
            # If the stack is empty after popping, it means we've found a complete group, so add it to the list of groups
            if not stack:
                groups.append(group)
                group = ""
    
    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses and iterates over the input string to separate the groups of nested parentheses. It removes any spaces from the input string and ignores any mismatched closing parentheses. The function returns a list of strings, each representing a separate group of nested parentheses.
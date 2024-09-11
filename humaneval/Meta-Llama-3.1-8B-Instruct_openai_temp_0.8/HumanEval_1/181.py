```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string to ignore them
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty stack to keep track of opening parentheses
    stack = []
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
            else:
                # If the stack is empty, it means we've found a complete group, so add it to the list and reset the current group
                groups.append(current_group)
                current_group = ""
        # If the stack is empty, it means we've found a complete group, so add it to the list and reset the current group
        if not stack:
            groups.append(current_group)
            current_group = ""
    
    # Return the list of separate groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups. It uses a stack to keep track of opening parentheses and a list to store the separate groups. The function iterates over the characters in the input string, pushing opening parentheses onto the stack and popping them when it encounters a closing parenthesis. If the stack is empty when it encounters a closing parenthesis, it means we've found a complete group, so it adds the current group to the list and resets the current group. Finally, it returns the list of separate groups.
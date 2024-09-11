```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses.
    It separates these groups into separate strings and returns the list of those.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings where each string is a separate group of nested parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize a stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we have found a complete group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means there's an extra closing parenthesis, ignore it
                continue
    
    # Return the list of separate groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the opening parentheses and a string to build the current group. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack. If the stack is empty after popping, it means we have found a complete group, so we add it to the list of groups and reset the current group.
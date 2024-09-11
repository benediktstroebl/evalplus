```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize a stack to keep track of opening parentheses
    stack = []
    
    # Initialize a list to store separate groups
    groups = []
    
    # Initialize a string to build the current group
    group = ""
    
    # Iterate over the characters in the input string
    for paren in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if paren == "(":
            stack.append(paren)
            group += paren
        # If the character is a closing parenthesis
        elif paren == ")":
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                group += paren
            # If the stack is empty, it means we've found a complete group
            else:
                groups.append(group)
                group = ""
    
    # If there are any remaining groups in the group string, add them to the list of groups
    if group:
        groups.append(group)
    
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
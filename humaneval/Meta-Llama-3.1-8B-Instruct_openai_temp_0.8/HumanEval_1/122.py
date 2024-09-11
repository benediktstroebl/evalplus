```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.
    """
    
    # Remove leading and trailing whitespaces
    paren_string = paren_string.strip()
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty stack to keep track of opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                current_group += char
            # If the stack is empty, it means the current group is complete, so add it to the list
            else:
                separate_groups.append(current_group)
                current_group = ''
        # If the character is not a parenthesis, ignore it
    
    # Return the list of separate groups
    return separate_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
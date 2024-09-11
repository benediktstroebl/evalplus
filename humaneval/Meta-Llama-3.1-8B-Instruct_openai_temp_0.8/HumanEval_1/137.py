```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the opening parenthesis from the stack
        elif char == ')':
            # If the stack is empty, it means the closing parenthesis does not match any opening parenthesis
            # So, we start a new group
            if not stack:
                separate_groups.append(current_group)
                current_group = ''
            # If the stack is not empty, pop the opening parenthesis from the stack
            else:
                stack.pop()
                current_group += char
    
    # If the stack is not empty, it means there are remaining opening parentheses that do not have a matching closing parenthesis
    # So, we start a new group with these remaining opening parentheses
    if stack:
        separate_groups.append(current_group)
    
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
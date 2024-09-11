```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced nested parentheses into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    
    # Initialize an empty list to store the grouped parentheses
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Initialize a stack to keep track of open parentheses
    stack = []
    
    # Iterate over each character in the input string
    for char in paren_string:
        
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            if stack:  # Check if the stack is not empty
                stack.pop()
                current_group += char
            
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                groups.append(current_group)
                current_group = ''
        
        # If the character is a space, ignore it
        elif char =='':
            continue
    
    # Return the list of grouped parentheses
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
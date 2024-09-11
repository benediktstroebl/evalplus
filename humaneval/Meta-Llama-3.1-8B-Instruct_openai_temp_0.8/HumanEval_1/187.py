```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses from a given string into a list of strings.
    
    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string represents a group of balanced parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            stack.pop()
            group += char
            # If the stack is now empty, it means we've found a balanced group
            if not stack:
                groups.append(group)
                group = ''
    
    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings where each string represents a group of balanced parentheses. The function uses a stack to keep track of the opening parentheses and a string to build the current group. When a balanced group is found, it is added to the list of groups. The function also removes any spaces from the input string before processing it.
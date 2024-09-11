```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and separates the groups into a list of strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string is a separate group of nested parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Initialize an empty stack to track the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add the closing parenthesis to the current group
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                separated_groups.append(current_group)
                current_group = ''
    
    # Return the list of separated groups
    return separated_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, removes any spaces, and separates the groups into a list of strings. It uses a stack to track the opening parentheses and a current group string to build each group. When a complete group is found, it's added to the list of separated groups. The function returns this list. The example usage at the end shows how to call the function with a sample input string.
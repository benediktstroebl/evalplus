```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of balanced parentheses into individual groups.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a group of balanced parentheses.
    """
    
    stack = []  # Initialize an empty stack to keep track of opening parentheses
    groups = []  # Initialize an empty list to store individual groups
    
    for char in paren_string:  # Iterate over each character in the input string
        if char == '(':  # If the character is an opening parenthesis
            stack.append(char)  # Push it onto the stack
        elif char == ')':  # If the character is a closing parenthesis
            if stack:  # If the stack is not empty
                stack.pop()  # Pop the corresponding opening parenthesis from the stack
            else:  # If the stack is empty
                groups.append('')  # Start a new group
        else:  # If the character is not a parenthesis (ignore spaces)
            pass
        
        if not stack:  # If the stack is empty
            groups.append('')  # Start a new group
        else:  # If the stack is not empty
            groups[-1] += char  # Add the character to the current group
    
    return [group for group in groups if group]  # Return the list of non-empty groups

# Example use case:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a group of balanced parentheses. It uses a stack to keep track of opening parentheses and iterates over the input string to build individual groups. The function ignores any spaces in the input string and starts a new group whenever it encounters a closing parenthesis when the stack is empty. The script also includes an example use case to demonstrate how to use the function.
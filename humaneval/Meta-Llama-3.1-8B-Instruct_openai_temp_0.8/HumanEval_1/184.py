```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    clean_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over the characters in the cleaned string
    for char in clean_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            stack.pop()
            current_group += char
            
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                # Add the current group to the list of separated groups
                separated_groups.append(current_group)
                # Reset the current group and the stack for the next iteration
                current_group = ""
                stack = []
    
    # Return the list of separated groups
    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( ")) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. The function uses a stack to keep track of the opening parentheses and a loop to iterate over the characters in the input string. When a complete group is found, it is added to the list of separated groups and the stack is reset for the next iteration. The function then returns the list of separated groups.
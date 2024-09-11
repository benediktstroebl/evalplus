```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses, 
    separates these groups into separate strings and returns the list of those.
    
    Parameters:
    paren_string (str): Input string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of separate groups of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add it to the current group
        elif char == ")":
            stack.pop()
            current_group += char
        # If the stack is empty after processing the current character, it means we've found a complete group
        if not stack:
            # Add the current group to the list of separated groups
            separated_groups.append(current_group)
            # Reset the current group and stack for the next group
            current_group = ""
            stack = []
    
    # Return the list of separated groups
    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
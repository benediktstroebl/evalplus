```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates multiple groups of nested parentheses in a string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize an empty stack to keep track of the parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char
        
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            stack.pop()
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                # Add the current group to the list of groups and reset the current group
                groups.append(current_group)
                current_group = ""
    
    # Return the list of separate groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
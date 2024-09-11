```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of multiple groups of nested parentheses into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of separate groups of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char
        
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            stack.pop()
            # If the stack is empty after popping, it means we have a complete group
            if not stack:
                # Add the current group to the list of separate groups
                separate_groups.append(current_group)
                # Reset the current group
                current_group = ""
    
    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and separates the string into groups of balanced parentheses. The function uses a stack to keep track of the opening parentheses and builds each group by adding characters to a string. When a complete group is found (i.e., the stack is empty after popping a closing parenthesis), the group is added to the list of separate groups. The function returns this list of separate groups.
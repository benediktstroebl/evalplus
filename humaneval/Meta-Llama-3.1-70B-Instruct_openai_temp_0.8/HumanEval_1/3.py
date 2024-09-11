```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of nested parentheses into separate groups.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty stack
    stack = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop from the stack
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty, it means we have found a complete group
            if not stack:
                result.append(current_group)
                current_group = ""
    
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
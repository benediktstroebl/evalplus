```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input.
    It separates those groups into separate strings and returns the list of those.
    
    Parameters:
    paren_string (str): The input string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                current_group += char
            # If the stack is empty, it means we've found a complete group, so add it to the result
            else:
                result.append(current_group)
                current_group = ""
    
    # If the stack is not empty, it means there are some unmatched opening parentheses left
    if stack:
        raise ValueError("Unmatched opening parentheses")
    
    # Return the list of complete groups
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string containing multiple groups of nested parentheses as input and returns a list of strings, each containing a separate group of nested parentheses. The function uses a stack to keep track of the opening parentheses and a list to store the result. It iterates over each character in the input string, pushing opening parentheses onto the stack and popping them when a matching closing parenthesis is found. If a complete group is found, it is added to the result list. If there are any unmatched opening parentheses left, a `ValueError` is raised. The script also includes a test case to verify the function's correctness.
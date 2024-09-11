```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a group of balanced nested parentheses.
    """
    
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack and a list to store the result
    stack = []
    result = []
    current_group = ""

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        # and add the close parenthesis to the current group
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have a complete group, so add it to the result
            if not stack:
                result.append(current_group)
                current_group = ""

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings where each string is a group of balanced nested parentheses. The function uses a stack to keep track of the open parentheses and a list to store the result. It iterates over each character in the string, pushing open parentheses onto the stack and popping them when it encounters a close parenthesis. When the stack is empty, it means we have a complete group, so we add it to the result.
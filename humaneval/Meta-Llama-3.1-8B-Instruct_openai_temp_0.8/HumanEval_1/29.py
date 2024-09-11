```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # Pop the corresponding opening parenthesis from the stack
            stack.pop()
            # If the stack is empty, it means we've found a complete group
            if not stack:
                # Add the current group to the result list
                result.append(current_group)
                # Reset the current group
                current_group = ''
            # If the stack is not empty, it means we haven't found a complete group yet
            else:
                # Add the closing parenthesis to the current group
                current_group += char

    # Return the list of groups
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the opening parentheses and checks if the stack is empty when it encounters a closing parenthesis. If the stack is empty, it means we've found a complete group and adds it to the result list. If the stack is not empty, it means we haven't found a complete group yet, so we add the closing parenthesis to the current group. Finally, it returns the list of groups.
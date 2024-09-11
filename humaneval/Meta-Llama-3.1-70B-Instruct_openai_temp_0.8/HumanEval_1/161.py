```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups of parentheses
    paren_groups = []

    # Initialize an empty stack to keep track of the opening and closing parentheses
    stack = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've reached the end of a group, so add it to the list
            # and reset the current group
            if not stack:
                paren_groups.append(current_group)
                current_group = ''

    # Return the list of separate groups of parentheses
    return paren_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script works by iterating over the input string and using a stack to keep track of the opening and closing parentheses. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack and checks if the stack is empty. If the stack is empty, it means we've reached the end of a group, so it adds the current group to the list and resets the current group. Finally, it returns the list of separate groups of parentheses.
### Separate Parenthesis Groups
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string and return them as a list.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of nested parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Initialize an empty list to store separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    groups.append(current_group)
                    current_group = ''
            # If the stack is empty, it means there's a mismatched closing parenthesis, so we ignore it
            else:
                current_group = ''

    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups. It uses a stack to keep track of opening parentheses and builds the current group by iterating over each character in the input string. When it finds a complete group (i.e., a well-formed pair of parentheses), it adds it to the list of groups and resets the current group. Finally, it returns the list of separated groups.
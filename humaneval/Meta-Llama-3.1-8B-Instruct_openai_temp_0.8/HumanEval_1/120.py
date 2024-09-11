```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of parenthesies.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a stack to keep track of opening parentheses
    opening_paren_stack = []

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            opening_paren_stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is empty, this parenthesis does not match any opening parenthesis
            if not opening_paren_stack:
                raise ValueError("Invalid parentheses in the input string")
            # Pop the matching opening parenthesis from the stack
            opening_paren_stack.pop()
            # Add the closing parenthesis to the current group
            current_group += char
            # If the stack is empty after popping, the current group is complete
            if not opening_paren_stack:
                # Add the complete group to the list of separated groups
                separated_groups.append(current_group)
                current_group = ''

    # If the stack is not empty after iterating over all characters, there are unmatched opening parentheses
    if opening_paren_stack:
        raise ValueError("Invalid parentheses in the input string")

    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. The function uses a stack to keep track of opening parentheses and a string to build the current group. When a matching closing parenthesis is encountered, the function adds the closing parenthesis to the current group and checks if the stack is empty. If the stack is empty, the current group is complete and is added to the list of separated groups. If there are unmatched opening parentheses at the end of the input string, the function raises a ValueError.
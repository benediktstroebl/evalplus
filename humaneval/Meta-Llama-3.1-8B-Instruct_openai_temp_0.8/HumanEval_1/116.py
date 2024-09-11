```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize stack to keep track of opening parentheses
    stack = []
    groups = []
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and append it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the opening parenthesis from the stack and append it to the current group
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    groups.append(current_group)
                    current_group = ''
            # If the stack is empty, it means we have a closing parenthesis without a matching opening one, so we ignore it
            else:
                continue

    # Return the list of separate groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups. It uses a stack to keep track of opening parentheses and a variable to hold the current group. When an opening parenthesis is encountered, it is pushed onto the stack and appended to the current group. When a closing parenthesis is encountered, the opening parenthesis is popped from the stack and appended to the current group. If the stack is empty after popping, it means we've found a complete group, which is added to the list of groups. If the stack is empty when a closing parenthesis is encountered, we ignore it. Finally, the list of separate groups is returned.
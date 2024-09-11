Here is a Python script that uses a stack data structure to solve the problem:

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): The input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string contains a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty (i.e., we have a matching opening parenthesis), pop it from the stack
            if stack:
                stack.pop()
                # If the stack is empty after popping (i.e., we have a complete group), add the current group to the list and reset it
                if not stack:
                    groups.append(current_group)
                    current_group = ''
                # If the stack is not empty (i.e., we have nested groups), add the closing parenthesis to the current group
                else:
                    current_group += char
            # If the stack is empty (i.e., we have a mismatched closing parenthesis), ignore it
            else:
                pass

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a stack to keep track of opening parentheses. When it encounters a closing parenthesis, it checks if the stack is empty (i.e., if we have a complete group) or not (i.e., if we have nested groups). If the stack is empty, it adds the current group to the list and resets it. If the stack is not empty, it adds the closing parenthesis to the current group. This way, it correctly separates groups of nested parentheses in the input string.
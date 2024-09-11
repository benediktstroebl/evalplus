```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate strings, each containing a group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty stack to keep track of opening parentheses
    stack = []
    # Initialize an empty string to build each group of parentheses
    group = ''
    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            # Add the character to the current group
            group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                # Add the character to the current group
                group += char
                # If the stack is now empty, the group is complete, so add it to the list
                if not stack:
                    separate_groups.append(group)
                    # Reset the group and stack for the next group
                    group = ''
                    stack = []

    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses as it iterates over each character in the input string. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack. If the stack becomes empty after a closing parenthesis is encountered, the current group is complete and is added to the list of separate groups. The group and stack are then reset to begin building the next group.
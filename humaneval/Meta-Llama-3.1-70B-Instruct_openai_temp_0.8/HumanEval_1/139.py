```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings, each representing a separate group of parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty stack to keep track of the parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            stack.pop()
        
        # Add the character to the current group
        current_group += char

        # If the stack is empty, it means we've found a complete group
        if not stack:
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group
            current_group = ''

    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
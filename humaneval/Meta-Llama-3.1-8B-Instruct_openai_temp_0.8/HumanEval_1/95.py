```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a group of balanced parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        if char == '(':
            # If an open parenthesis is encountered, increment the balance counter
            balance += 1
            current_group += char
        elif char == ')':
            # If a close parenthesis is encountered, decrement the balance counter
            balance -= 1
            current_group += char

            # If the balance counter is zero, it means we have a complete group
            if balance == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group and balance counter
                current_group = ''
                balance = 0

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and separates the groups of balanced parentheses into individual strings. The function uses a simple counter-based approach to track the balance of parentheses and build the current group. When a complete group is detected (i.e., the balance counter is zero), it is added to the list of groups. Finally, the script tests the function with the provided example.
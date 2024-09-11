```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, separates the groups, 
    and returns them as a list of strings.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            current_group += char
            # If the balance is zero, it means we have a complete group
            if balance == 0:
                # Add the current group to the list of separate groups
                separate_groups.append(current_group)
                # Reset the current group and balance
                current_group = ''
                balance = 0

    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, separates the groups, and returns them as a list of strings. It uses a balance counter to keep track of the parentheses balance and a current group string to build each separate group. When a complete group is found, it is added to the list of separate groups and the current group is reset. The function is tested with the example provided.
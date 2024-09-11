```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into a list of strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
            # Add the character to the current group
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            # Add the character to the current group
            current_group += char
        # If the balance is zero, it means we've found a complete group
        if balance == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group and balance
            current_group = ''
            balance = 0

    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack-based approach to separate the groups of balanced parentheses from the input string. It iterates over each character in the string, keeping track of the balance of open and close parentheses. When the balance becomes zero, it means we've found a complete group, so it adds the current group to the list of groups and resets the current group and balance. Finally, it returns the list of separated groups.
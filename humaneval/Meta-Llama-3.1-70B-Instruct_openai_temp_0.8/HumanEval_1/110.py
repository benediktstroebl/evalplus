```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate a string containing multiple groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups of parentheses
    separate_groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ''

    # Initialize a counter to keep track of the balance of open and close parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance counter
        if char == '(':
            balance += 1
        # If the character is a close parenthesis, decrement the balance counter
        elif char == ')':
            balance -= 1

        # Add the character to the current group
        current_group += char

        # If the balance counter is zero, it means we have a complete group of parentheses
        if balance == 0:
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group
            current_group = ''

    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
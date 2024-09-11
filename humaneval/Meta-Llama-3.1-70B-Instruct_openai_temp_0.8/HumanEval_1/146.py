```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups of parentheses
    groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1

        # If the balance is zero, it means we've found a complete group of parentheses
        if balance == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group and balance
            current_group = ''
            balance = 0

    # Return the list of separate groups of parentheses
    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
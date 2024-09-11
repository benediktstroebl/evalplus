```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses in the current group
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            current_group += char

            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group and balance
                current_group = ''
                balance = 0

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to separate the groups of parentheses. It keeps track of the balance of parentheses and adds the current group to the list when the balance reaches zero. The script also removes any spaces from the input string and handles the case where there are multiple groups at the end of the string.
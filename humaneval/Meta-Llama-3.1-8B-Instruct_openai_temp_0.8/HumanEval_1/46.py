```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates balanced groups of nested parentheses in a string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, where each string is a separate group of balanced parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, increase the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrease the balance
        elif char == ')':
            balance -= 1
            current_group += char
            # If the balance is zero, it means we have a complete group, so add it to the list and reset the current group
            if balance == 0:
                separated_groups.append(current_group)
                current_group = ''

    # Return the list of separated groups
    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and then iterates over each character in the string. It keeps track of the balance of open and close parentheses and uses this balance to determine when a complete group has been found. It then adds this group to the list of separated groups and continues with the next character. The function returns this list of separated groups.
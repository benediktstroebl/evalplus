```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses into separate strings and returns them as a list.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty string to store the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increase the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrease the balance
        elif char == ')':
            balance -= 1
            current_group += char
            # If the balance is zero, it means we've found a complete group, so add it to the result and reset the current group
            if balance == 0:
                result.append(current_group)
                current_group = ''

    # Return the result
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over each character in the input string, keeping track of the balance of parentheses. When the balance is zero, it means we've found a complete group, so we add it to the result and reset the current group. At the end, the function returns the list of complete groups.
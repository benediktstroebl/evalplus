```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into individual strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build each group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
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
            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ''

    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of nested parentheses. The function uses a balance counter to keep track of the nesting of parentheses, and it builds each group by concatenating characters to the `current_group` string. When a closing parenthesis is encountered and the balance reaches zero, it means we've found a complete group, so we add the current group to the `groups` list and reset the `current_group` string.
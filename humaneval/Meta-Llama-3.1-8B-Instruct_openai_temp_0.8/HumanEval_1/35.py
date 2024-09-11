```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and returns a list of separate groups.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a separate group of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            current_group += char

            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                separate_groups.append(current_group)
                current_group = ''

    return separate_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a simple iterative approach to separate the groups of parentheses. It maintains a balance counter to keep track of whether the current group is balanced. When the balance becomes zero, it means we've reached the end of a group, and we can add it to the list of separate groups.
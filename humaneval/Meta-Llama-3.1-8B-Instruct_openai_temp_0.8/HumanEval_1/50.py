```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input, 
    separates these groups into separate strings, and returns the list of those groups.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the groups of parentheses
    groups = []

    # Initialize an empty string to build the current group of parentheses
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
            # If the balance is zero, it means we've found a complete group of parentheses
            if balance == 0:
                groups.append(current_group)
                current_group = ''

    # Return the list of groups of parentheses
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to solve the problem. It iterates over each character in the input string, keeping track of the balance of parentheses. When it encounters a close parenthesis and the balance is zero, it means it has found a complete group of parentheses, so it adds that group to the list of groups.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses into different strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string contains a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the balance is 0, it means we've found a complete group
            if balance == 0:
                separate_groups.append(current_group)
                current_group = ""
            # Otherwise, decrement the balance and add the closing parenthesis to the current group
            else:
                balance -= 1
                current_group += char

    # Return the list of separate groups
    return separate_groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings where each string contains a separate group of nested parentheses. It does this by incrementing a balance counter whenever it encounters an opening parenthesis and decrementing it whenever it encounters a closing parenthesis. When the balance reaches 0, it means a complete group has been found, and the current group is added to the list of separate groups.
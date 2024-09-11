```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.

    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char

        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char

            # If the balance is zero, it means we have a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and then iterates over the characters to find separate groups of balanced parentheses. It uses a balance counter to keep track of the parentheses and appends each group to the result list when it finds a complete group. Finally, it returns the list of separated groups.
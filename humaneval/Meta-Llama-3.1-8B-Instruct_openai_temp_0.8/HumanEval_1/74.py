```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups
    groups = []

    # Initialize an empty string to build the current group
    group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increase the balance
        if char == "(":
            balance += 1
            group += char
        # If the character is a close parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            group += char
        # If the balance is zero, it means we've found a complete group
        if balance == 0:
            # Add the group to the list of groups
            groups.append(group)
            # Reset the group and balance
            group = ""
            balance = 0

    # Return the list of groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of nested parentheses. It uses a simple counter-based approach to keep track of the balance of parentheses and build the groups. The script also includes a test case to demonstrate the function's behavior.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings and returns them as a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group and balance
                current_group = ""
                balance = 0

    # If there are any remaining characters in the current group, it means the input string was not properly balanced
    if current_group:
        raise ValueError("Input string is not properly balanced")

    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of nested parentheses. The function uses a stack-based approach to keep track of the balance of parentheses and separate the groups. It also removes any spaces from the input string and handles the case where the input string is not properly balanced.
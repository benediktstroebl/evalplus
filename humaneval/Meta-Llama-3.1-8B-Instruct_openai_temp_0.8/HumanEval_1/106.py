```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of strings, each containing a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            # Add the character to the current group
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            # Add the character to the current group
            current_group += char
            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                # Add the current group to the list of separate groups
                separate_groups.append(current_group)
                # Reset the current group and balance
                current_group = ""
                balance = 0

    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to separate the groups of nested parentheses. It keeps track of the balance of parentheses and adds a group to the list when the balance is zero. The script ignores any spaces in the input string and returns a list of strings, each containing a separate group of nested parentheses.
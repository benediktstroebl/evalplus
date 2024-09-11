```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

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

        # If the balance is zero, it means we've finished a separate group
        if balance == 0:
            separate_groups.append(current_group)
            current_group = ""

    return separate_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over each character in the input string. When it encounters an open parenthesis, it adds the parenthesis to the current group and increments the balance. When it encounters a close parenthesis, it adds the parenthesis to the current group and decrements the balance. When the balance becomes zero, it means we've finished a separate group, so we add the current group to the list of separate groups and reset the current group.
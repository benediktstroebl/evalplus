```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.
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
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1

        # If the balance is zero, it means we have a complete group
        if balance == 0:
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group
            current_group = ""

    return separate_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
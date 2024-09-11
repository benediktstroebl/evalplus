### Separate Paren Groups
#### Solution

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from a given string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string contains a group of balanced parentheses.
    """
    # Remove spaces from the input string
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

            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group and balance
                current_group = ""
                balance = 0

    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to separate the groups of balanced parentheses from the input string. It keeps track of the balance of parentheses using a counter and adds the current group to the list of groups whenever it finds a complete group. The script returns a list of strings where each string contains a group of balanced parentheses.
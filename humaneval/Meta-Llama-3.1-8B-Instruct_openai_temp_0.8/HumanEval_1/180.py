```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store separate groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char

            # If the balance becomes zero, it means we have found a separate group
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and separates the groups of balanced parentheses into a list of strings. It uses a counter to keep track of the balance of parentheses and starts a new group whenever the balance becomes zero. The function returns the list of separate groups. The test case is provided at the end of the script.
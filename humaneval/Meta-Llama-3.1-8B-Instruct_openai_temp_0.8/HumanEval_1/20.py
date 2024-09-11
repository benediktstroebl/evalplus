```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of string groups separated by balanced and non-nested parentheses.
    """
    # Remove spaces from the string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate over the characters in the string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char

        # If the balance is zero, it means we've found a complete group
        if balance == 0:
            groups.append(current_group)
            current_group = ""

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over the characters in the input string and keeping track of the balance of parentheses. When the balance reaches zero, it means we've found a complete group, which is then added to the list of groups.
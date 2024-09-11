```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of nested parentheses as strings.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance and add to the current group
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrease the balance and add to the current group
        elif char == ")":
            balance -= 1
            current_group += char
        # If the character is not a parenthesis, skip it
        else:
            continue

        # If the balance reaches zero, it means we've found a complete group, so add it to the list and reset the current group
        if balance == 0:
            separated_groups.append(current_group)
            current_group = ""

    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a simple iterative approach to separate the groups of parentheses. It keeps track of the balance of parentheses and adds characters to the current group until the balance reaches zero, at which point it adds the group to the list of separated groups and resets the current group.
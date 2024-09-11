```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups
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
                groups.append(current_group)
                current_group = ""

    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each representing a group of nested parentheses. The function iterates over the input string, keeping track of the balance of parentheses and building up the current group. When a complete group is found, it is added to the list of groups. The function then returns the list of groups. The test case at the end demonstrates the function's behavior.
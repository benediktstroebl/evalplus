```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses and separates it into a list of balanced groups.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of balanced groups of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to track the balance of parentheses
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

            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, removes any spaces, and separates it into a list of balanced groups. It does this by iterating over each character in the input string, incrementing a balance counter when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. When the balance reaches zero, it means we've found a complete group, so we add it to the list of groups and reset the current group. Finally, we return the list of groups.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, separates them into balanced groups, 
    and returns the list of those groups.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a balanced group of parentheses.

    """
    
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the balanced groups
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
            # Add the open parenthesis to the current group
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            # Add the close parenthesis to the current group
            current_group += char
            # If the balance is now zero, it means we've found a complete group
            if balance == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group and balance
                current_group = ""
                balance = 0

    # If the final balance is not zero, it means the input string is not properly balanced
    if balance!= 0:
        raise ValueError("Input string is not properly balanced")

    # Return the list of balanced groups
    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, separates them into balanced groups, and returns the list of those groups. It uses a simple iterative approach to keep track of the balance of parentheses and build the current group. If the input string is not properly balanced, it raises a `ValueError`. The example usage at the end demonstrates how to use this function.
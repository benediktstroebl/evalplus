```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of balanced nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of balanced nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance counter
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance counter
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance counter is zero, it means we have a complete group
            if balance == 0:
                # Add the complete group to the list and reset the current group
                separate_groups.append(current_group)
                current_group = ""

    # Return the list of separated groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of balanced parentheses as input and returns a list of strings where each string is a separate group of balanced parentheses. The function iterates over the input string, keeping track of the balance of parentheses, and builds a string representing a group of balanced parentheses. When the balance counter reaches zero, it means we have a complete group, which is added to the list and the current group is reset. The function finally returns the list of separated groups.
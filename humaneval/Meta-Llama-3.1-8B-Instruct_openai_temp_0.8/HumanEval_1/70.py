```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, where each string is a group of balanced nested parentheses.
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
            # If the balance is zero, it means we've found a complete group, so add it to the list
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    # Return the list of separated groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of balanced nested parentheses as input and returns a list of separate groups. It uses a counter to keep track of the balance of parentheses and builds each group by accumulating characters until the balance reaches zero. The function then adds the complete group to the list and starts building the next group.
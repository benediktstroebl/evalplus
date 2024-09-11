```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of separate groups of nested parentheses.

    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate over the characters in the string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""
        # If the character is not a parenthesis, ignore it

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over the input string and building groups of nested parentheses. It uses a balance counter to keep track of the number of opening and closing parentheses. When the balance becomes zero, it means we've found a complete group, which is then added to the list of groups. The script ignores any spaces in the input string and returns the list of separate groups.
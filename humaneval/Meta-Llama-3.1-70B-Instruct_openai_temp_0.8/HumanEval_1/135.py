```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of parentheses as input, separates them into groups 
    and returns a list of strings, each representing a group of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    paren_groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1

        # If the balance is zero, it means we have a complete group of parentheses
        if balance == 0:
            # Add the current group to the list of groups and reset the current group
            paren_groups.append(current_group)
            current_group = ""

    # Return the list of groups
    return paren_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
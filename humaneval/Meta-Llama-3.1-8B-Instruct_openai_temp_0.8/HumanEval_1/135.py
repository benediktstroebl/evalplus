```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the parentheses balance
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char

        # If the character is a close parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char

        # If the balance is zero, it means we've found a complete group
        if balance == 0:
            # Add the current group to the list of separated groups
            separated_groups.append(current_group)
            # Reset the current group and balance
            current_group = ""
            balance = 0

    # Return the list of separated groups
    return separated_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. The function uses a counter to keep track of the balance of parentheses and builds the current group as it iterates over the input string. When a complete group is found, it is added to the list of separated groups and the current group and balance are reset. Finally, the list of separated groups is returned.
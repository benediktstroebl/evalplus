```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced parentheses from a given string into a list.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char

        # If the balance is zero, it means we have a complete group
        if balance == 0:
            groups.append(current_group)
            current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, where each string represents a group of balanced parentheses. It uses a counter to keep track of the balance of parentheses and appends characters to the current group as long as the balance is non-zero. When the balance is zero, it means we have a complete group, so we append it to the list of groups and reset the current group.
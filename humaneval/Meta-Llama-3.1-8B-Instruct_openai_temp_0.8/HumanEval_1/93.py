### Separate Parenthesis Groups
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced, non-nested, nested parentheses from a string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, where each string represents a group of balanced, non-nested, nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the parenthesis balance
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

            # If the balance is zero, it means we have a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over each character in the input string. It keeps track of the balance of open and close parentheses. When the balance is zero, it means we have a complete group, so we add the current group to the list and reset the current group. The function finally returns the list of separated groups.
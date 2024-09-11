```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                separated_groups.append(current_group)
                current_group = ""

    # Return the list of separated groups
    return separated_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that separates groups of nested parentheses in a given string into separate strings. It uses a stack-like approach to track the balance of parentheses and build the current group. When a complete group is found, it is added to the list of separated groups. The function returns the list of separated groups. The test case at the end demonstrates the function's usage.
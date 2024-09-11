```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separate groups of nested parentheses as strings.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to track the balance of parentheses
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
        # If the balance is 0, it means we've found a separate group
        if balance == 0:
            separate_groups.append(current_group)
            current_group = ""

    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to separate groups of nested parentheses. It keeps track of the balance of parentheses and uses it to determine when a separate group has been found. The function ignores any spaces in the input string and returns a list of separate groups as strings. The test case at the end demonstrates the function's correctness.
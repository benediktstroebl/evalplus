```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): The string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, where each string represents a group of parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize a list to store the separated parenthesis groups
    groups = []

    # Initialize a counter to keep track of the balance of the parentheses
    balance = 0

    # Initialize a string to store the current group of parentheses
    current_group = ""

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance counter
        if char == "(":
            balance += 1
        # If the character is a closing parenthesis, decrement the balance counter
        elif char == ")":
            balance -= 1

        # Add the character to the current group of parentheses
        current_group += char

        # If the balance is zero, it means we've found a complete group of parentheses
        if balance == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""

    # Return the list of separated parenthesis groups
    return groups


# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
```
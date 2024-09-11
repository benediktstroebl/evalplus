```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separated strings, each containing a group of nested parentheses.
    """

    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
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

            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                separated_groups.append(current_group)
                current_group = ""

    # Return the list of separated groups
    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This Python script defines a function `separate_paren_groups` that takes a string of nested parentheses and returns a list of separated strings, each containing a group of balanced parentheses. It uses a balance counter to keep track of the number of open and close parentheses, adding the current group to the list when the balance reaches zero. The function then returns the list of separated groups.
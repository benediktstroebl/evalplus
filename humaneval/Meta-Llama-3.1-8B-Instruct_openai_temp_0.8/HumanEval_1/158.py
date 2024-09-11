```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings and returns them as a list.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings where each string represents a group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance is zero, it means we have a complete group, so add it to the list and reset the current group
            if balance == 0:
                separated_groups.append(current_group)
                current_group = ""

    # Return the list of separated groups
    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script will output:
```python
['()', '(())', '(()())']
```
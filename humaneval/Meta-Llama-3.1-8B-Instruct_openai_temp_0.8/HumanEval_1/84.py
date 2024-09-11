```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates the groups of balanced parentheses in a string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrease the balance
        elif char == ')':
            balance -= 1
            current_group += char

            # If the balance becomes zero, it means we've reached the end of a group
            if balance == 0:
                separate_groups.append(current_group)
                current_group = ''

    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script first removes any spaces from the input string. It then initializes an empty list to store the separate groups and an empty string to build the current group. It also initializes a counter to keep track of the balance of parentheses.

The script then iterates over the characters in the input string. If it encounters an opening parenthesis, it increases the balance and adds the character to the current group. If it encounters a closing parenthesis, it decreases the balance, adds the character to the current group, and checks if the balance has become zero. If the balance has become zero, it means we've reached the end of a group, so it adds the current group to the list of separate groups and resets the current group.

Finally, the script returns the list of separate groups.
```python
from typing import List
import itertools


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separate groups of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the groups
    groups = []

    # Initialize an index to track the current position in the string
    i = 0

    # Iterate over the string
    while i < len(paren_string):
        # If the current character is an open parenthesis, start a new group
        if paren_string[i] == '(':
            group = ''
            # Move to the corresponding closing parenthesis
            for j in range(i, len(paren_string)):
                if paren_string[j] == ')':
                    # Extract the group and add it to the list
                    groups.append(paren_string[i:j+1])
                    # Move the index to the position after the closing parenthesis
                    i = j + 1
                    break
                else:
                    # If not a closing parenthesis, add the current character to the group
                    group += paren_string[j]
        else:
            # If the current character is not an open parenthesis, move to the next character
            i += 1

    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over the string and identifying the groups of parentheses. When an open parenthesis is encountered, it starts a new group and moves to the corresponding closing parenthesis. The group is then added to the list and the index is moved to the position after the closing parenthesis.
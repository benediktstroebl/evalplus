```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of balanced nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize a counter to keep track of the current group
    group_counter = 0

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, start a new group
        if char == '(':
            group_counter += 1
            # If this is not the first character in the group, add it to the current group
            if current_group:
                current_group += char
            # If this is the first character in the group, start a new group in the list
            else:
                groups.append(current_group)
                current_group = char
        # If the character is a close parenthesis, end the current group
        elif char == ')':
            # If the current group is not empty, add the close parenthesis to it
            if current_group:
                current_group += char
            # If the current group is empty, it means there was a close parenthesis without a matching open parenthesis, so ignore it
            else:
                continue
            # If this is not the last group, add it to the list
            if group_counter > 1:
                groups.append(current_group)
            # If this is the last group, reset the counter and the current group
            else:
                group_counter = 0
                current_group = ''
        # If the character is not a parenthesis, ignore it
        else:
            continue

    # Return the list of separated groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script separates groups of balanced nested parentheses in a string into separate strings. It iterates over each character in the input string and keeps track of the current group. When an open parenthesis is encountered, it starts a new group. When a close parenthesis is encountered, it ends the current group. The script ignores any spaces in the input string and any close parentheses without a matching open parenthesis. The example usage at the end demonstrates how to use the script with the provided example input.
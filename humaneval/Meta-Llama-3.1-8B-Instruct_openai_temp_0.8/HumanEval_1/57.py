```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string contains one separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == '(':
            current_group += char
        # If the character is a close parenthesis, add it to the current group and add the group to the list
        elif char == ')':
            current_group += char
            separate_groups.append(current_group)
            current_group = ''
        # If the character is neither an open nor close parenthesis, ignore it

    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups. It first removes any spaces from the input string, then iterates over each character. When it encounters an open parenthesis, it adds it to the current group. When it encounters a close parenthesis, it adds it to the current group and adds the current group to the list of separate groups. It then resets the current group. Finally, it returns the list of separate groups. The function is tested with the example provided in the problem statement.
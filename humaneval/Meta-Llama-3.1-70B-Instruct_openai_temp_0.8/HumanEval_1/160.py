```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    :param paren_string: A string containing multiple groups of nested parentheses
    :return: A list of strings, each representing a separate group of parentheses
    """
    paren_string = paren_string.replace(' ', '')  # Remove any spaces from the string
    groups = []
    current_group = ''
    open_braces = 0

    for char in paren_string:
        current_group += char
        if char == '(':
            open_braces += 1
        elif char == ')':
            open_braces -= 1
            if open_braces == 0:
                groups.append(current_group)
                current_group = ''

    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # ['()', '(())', '(()())']
```

This script works by iterating through the input string and maintaining a count of open parentheses. When the count reaches zero (i.e., all open parentheses have been closed), it adds the current group to the list of groups and resets the current group. The script also removes any spaces from the input string before processing it.
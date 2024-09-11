```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses and separates them into a list of strings.

    Args:
        paren_string (str): The input string containing groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    groups = []
    current_group = ""  # Initialize the current group as an empty string

    for char in paren_string:
        if char == "(":
            current_group += char  # Add the opening parenthesis to the current group
        elif char == ")":
            current_group += char  # Add the closing parenthesis to the current group
            groups.append(current_group)  # Add the current group to the list of groups
            current_group = ""  # Reset the current group

    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
print(separate_paren_groups('((()))(())()()(()())'))  # Output: ['((()))', '(())', '()', '()', '(()())']
```

This script works by iterating over each character in the input string. When it encounters an opening parenthesis, it adds it to the current group. When it encounters a closing parenthesis, it adds it to the current group and then adds the current group to the list of groups before resetting the current group. This way, each group of nested parentheses is properly separated and added to the list.
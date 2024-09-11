```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize variables to store the result and the current group
    result = []
    current_group = ''

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over the characters in the string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a closing parenthesis, decrease the nesting level
        elif char == ')':
            nesting_level -= 1

        # Add the character to the current group
        current_group += char

        # If the nesting level is zero, it means we've finished a group
        if nesting_level == 0:
            # Add the group to the result list
            result.append(current_group)
            # Reset the current group
            current_group = ''

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
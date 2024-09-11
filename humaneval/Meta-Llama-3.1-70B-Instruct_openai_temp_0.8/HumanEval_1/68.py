```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_group = ''
    open_count = 0

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Iterate over each character in the string
    for char in paren_string:
        current_group += char  # Add the character to the current group
        if char == '(':  # If the character is an open parenthesis, increment the count
            open_count += 1
        elif char == ')':  # If the character is a close parenthesis, decrement the count
            open_count -= 1
            if open_count == 0:  # If the count is zero, it means we've found a complete group
                result.append(current_group)  # Add the group to the result list
                current_group = ''  # Reset the current group

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Expected output: ['()', '(())', '(()())']
```
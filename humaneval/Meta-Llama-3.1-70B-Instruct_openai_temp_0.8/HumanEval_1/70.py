```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): The input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables to keep track of the result and the current group
    result = []
    current_group = ""
    open_count = 0

    # Iterate over the characters in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the count
        if char == "(":
            open_count += 1
        # If the character is a close parenthesis, decrement the count
        elif char == ")":
            open_count -= 1
            # If the count is zero, it means we've found a complete group
            if open_count == 0:
                # Add the group to the result list and reset the current group
                result.append(current_group)
                current_group = ""

    return result

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of parentheses.
    """
    result = []
    temp = ""
    count = 0

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Iterate over the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the count
        if char == "(":
            count += 1
        # If the character is a close parenthesis, decrement the count
        elif char == ")":
            count -= 1
        # Add the character to the temporary string
        temp += char
        # If the count is zero, it means we've found a complete group of parentheses
        if count == 0:
            # Add the group to the result list and reset the temporary string
            result.append(temp)
            temp = ""

    return result


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and then iterates over the string, using a counter to keep track of the nesting level of the parentheses. Whenever the counter reaches zero, it means a complete group of parentheses has been found, so the group is added to the result list and the temporary string is reset. The function finally returns the list of separate groups of parentheses.
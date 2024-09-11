```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of parentheses.

    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    result = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Initialize a counter to keep track of the nesting level of the parentheses
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1

        # Add the character to the current group of parentheses
        current_group += char

        # If the nesting level is zero, it means we've reached the end of a group of parentheses
        if nesting_level == 0:
            # Add the current group of parentheses to the result list
            result.append(current_group)
            # Reset the current group of parentheses
            current_group = ""

    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and then iterates over the string, using a nesting level counter to determine when a group of parentheses has been closed. When a group has been closed, it is added to the result list. The function then returns the list of groups of parentheses.
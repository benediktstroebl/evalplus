```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    :param paren_string: A string containing multiple groups of nested parentheses
    :return: A list of strings where each string is a separate group of balanced parentheses
    """
    # Remove spaces from the string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables to keep track of the current group and the list of groups
    current_group = ""
    groups = []

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1

        # If the nesting level is 0, it means we have a complete group
        if nesting_level == 0:
            # Add the group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""

    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
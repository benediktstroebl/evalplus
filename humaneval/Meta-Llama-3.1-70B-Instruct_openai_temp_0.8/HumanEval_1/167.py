```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses 
    into separate strings and returns the list of those.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to track the nesting level of the parentheses
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a closing parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1

        # Add the character to the current group
        current_group += char

        # If the nesting level is back to 0, it means we've found a complete group
        if nesting_level == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""

    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
```
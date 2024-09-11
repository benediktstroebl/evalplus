```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings where each string is a separate group of parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups of parentheses
    paren_groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Initialize a counter to keep track of the nesting level of parentheses
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

        # If the nesting level is zero, it means we have a complete group of parentheses
        if nesting_level == 0:
            # Add the current group to the list of groups and reset the current group
            paren_groups.append(current_group)
            current_group = ""

    # Return the list of separate groups of parentheses
    return paren_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
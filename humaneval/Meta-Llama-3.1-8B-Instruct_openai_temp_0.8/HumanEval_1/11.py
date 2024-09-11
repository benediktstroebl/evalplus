```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a group of nested parentheses.
    """
    
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the nesting level and add the character to the current group
        if char == "(":
            nesting_level += 1
            current_group += char
        
        # If the character is a closing parenthesis, decrease the nesting level
        elif char == ")":
            nesting_level -= 1
        
        # If the nesting level is zero, it means we've found a complete group, so add it to the list and reset the current group
        if nesting_level == 0:
            separated_groups.append(current_group)
            current_group = ""

    # Return the list of separated groups
    return separated_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string containing multiple groups of nested parentheses as input and returns a list of strings, each containing a group of nested parentheses. The function works by iterating over the input string, keeping track of the nesting level, and adding characters to a current group until a complete group is found. The complete group is then added to the list of separated groups and the current group is reset.
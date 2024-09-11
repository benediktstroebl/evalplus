```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to keep track of the opening and closing parentheses
    nesting_level = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
            # Add the character to the current group
            current_group += char
        # If the character is a closing parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1
            # Add the character to the current group
            current_group += char
            # If the nesting level is zero, it means we've found a complete group
            if nesting_level == 0:
                # Add the current group to the list of separate groups
                separate_groups.append(current_group)
                # Reset the current group
                current_group = ""
    
    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate groups of nested parentheses. The function iterates over each character in the input string, keeping track of the nesting level and building the current group. When a complete group is found (i.e., the nesting level is zero), it is added to the list of separate groups. The function finally returns the list of separate groups.
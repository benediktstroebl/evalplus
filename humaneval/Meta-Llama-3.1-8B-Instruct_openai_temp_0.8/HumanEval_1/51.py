```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, separates the groups into individual strings,
    and returns them as a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    # Remove leading and trailing spaces from the input string
    paren_string = paren_string.strip()
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == '(':
            current_group += char
        # If the character is a close parenthesis, add it to the current group and add the group to the list
        elif char == ')':
            current_group += char
            groups.append(current_group)
            current_group = ''
    
    # If the input string was empty or only contained open parentheses, add the current group to the list
    if current_group:
        groups.append(current_group)
    
    # Return the list of separate groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, separates the groups into individual strings, and returns them as a list. The function iterates over each character in the input string, building the current group of parentheses. When it encounters a close parenthesis, it adds the current group to the list and resets the current group. Finally, it returns the list of separate groups. The script includes a test case to demonstrate the function's behavior.
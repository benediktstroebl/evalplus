```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses from a given string.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a group of balanced nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to track the balance of parentheses
    balance = 0
    
    # Iterate over the characters in the input string
    for char in paren_string:
        
        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        
        # If the character is a closing parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char
        
        # If the balance is 0, it means we've found a complete group
        if balance == 0:
            separate_groups.append(current_group)
            current_group = ""
    
    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes spaces, and separates the groups of balanced parentheses into a list of strings. The function iterates over the characters in the input string, using a balance counter to track the nesting level of parentheses. When the balance counter reaches 0, it means a complete group has been found, and the function adds it to the list of separate groups. Finally, the function returns the list of separate groups.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the group of parentheses
    groups = []
    
    # Initialize an empty string to build a group of parentheses
    current_group = ''
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            current_group += char
            
            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ''
    
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. It iterates over the input string, building a group of parentheses by keeping track of the balance of open and close parentheses. When a complete group is found (i.e., the balance is zero), it is added to the list of groups and a new group is started. Finally, the function returns the list of groups.
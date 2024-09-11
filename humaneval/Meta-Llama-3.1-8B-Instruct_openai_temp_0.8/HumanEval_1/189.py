```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Initialize a counter to track the balance of parentheses in the current group
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance
        if char == '(':
            current_group += char
            balance += 1
        # If the character is a closing parenthesis, decrease the balance
        elif char == ')':
            current_group += char
            balance -= 1
            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group and balance
                current_group = ''
                balance = 0
    
    # Return the list of groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a counter to track the balance of parentheses in the current group. When the balance is zero, it means we've reached the end of a group, so the current group is added to the list of groups and the current group and balance are reset. This way, we can correctly separate the groups of parentheses in the input string.
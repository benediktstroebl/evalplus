```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input, 
    and returns a list of strings where each group is separated into a separate string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each group is separated into a separate string.
    """
    
    # Remove leading and trailing spaces from the input string
    paren_string = paren_string.strip()
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        
        # If the character is an open parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char
        
        # If the character is a close parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char
            
            # If the balance is zero, it means we've reached the end of a group, so add it to the list
            if balance == 0:
                groups.append(current_group)
                current_group = ""
    
    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings where each group is separated into a separate string. It does this by iterating over the input string and keeping track of the balance of parentheses. When the balance is zero, it means we've reached the end of a group, so we add it to the list. Finally, it returns the list of separated groups.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of balanced nested parentheses into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string contains a separate group of parentheses.
    """
    
    # Remove spaces from the string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the groups
    groups = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                # Add the current group to the list and reset it
                groups.append(current_group)
                current_group = ""
    
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script defines a function `separate_paren_groups` that takes a string of balanced nested parentheses and returns a list of strings where each string contains a separate group of parentheses. It uses a counter to keep track of the balance of parentheses and iterates over each character in the string to separate the groups. The function is then tested with the provided example.
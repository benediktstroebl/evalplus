```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses, 
    separates those groups into separate strings and returns the list of those.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups of parentheses
    separate_groups = []
    
    # Initialize an empty string to build each separate group of parentheses
    current_group = ""
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char
        
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
        
        # If the balance is zero, it means we have found a complete group of parentheses
        if balance == 0:
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group and the balance
            current_group = ""
    
    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # ['()', '(())', '(()())']
```
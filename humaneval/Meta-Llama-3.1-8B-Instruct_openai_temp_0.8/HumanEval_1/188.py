```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings where each string represents a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups of parentheses
    separate_groups = []
    
    # Initialize an empty string to build the current group of parentheses
    current_group = ""
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char
            
            # If the balance is zero, it means we have a complete group of parentheses
            if balance == 0:
                separate_groups.append(current_group)
                current_group = ""
    
    # Return the list of separate groups of parentheses
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate groups of parentheses. It iterates over each character in the input string, keeping track of the balance of parentheses and building the current group of parentheses. When a complete group is found (i.e., the balance is zero), it is added to the list of separate groups. The script then tests the function with the provided example.
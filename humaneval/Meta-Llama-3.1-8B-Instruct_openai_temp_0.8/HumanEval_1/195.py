```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of multiple groups of nested parentheses, 
    separates them into individual strings and returns a list of those strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Initialize a counter to track the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            current_group += char
            # If the balance is zero, it means we've found a complete group
            if balance == 0:
                # Add the current group to the list and reset it
                groups.append(current_group)
                current_group = ''
    
    # Return the list of separate groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups. It uses a simple stack-like approach to track the balance of parentheses and separate the groups. The function is well-documented with a docstring that explains its purpose and usage. The test case at the end demonstrates how to use the function.
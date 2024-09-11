```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string and returns them as a list of strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty string to build the current group
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
        
        # If the balance is 0, it means we have found a complete group, so add it to the list and reset the current group
        if balance == 0:
            groups.append(current_group)
            current_group = ""
    
    return groups

# Test the function
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a stack-like approach to separate the groups of parentheses. It iterates over each character in the input string, incrementing the balance when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. When the balance is 0, it means we have found a complete group, so it adds it to the list and resets the current group.
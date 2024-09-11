```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): Input string containing groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to track the balance of parentheses
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

This script uses a simple iterative approach to separate the groups of parentheses. It maintains a balance counter and a current group string. When an open parenthesis is encountered, the balance is increased and the character is added to the current group string. When a close parenthesis is encountered, the balance is decreased and the character is added to the current group string. If the balance becomes zero, it means we've reached the end of a group, so the current group string is added to the list of groups and reset.
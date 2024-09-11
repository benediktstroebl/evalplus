```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of balanced parentheses and separates them into distinct groups.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a balanced group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # If the balance is zero, this parenthesis does not have a matching open parenthesis
            if balance == 0:
                raise ValueError("Unbalanced parentheses: ')' without matching '('")
            # Decrement the balance and add the close parenthesis to the current group
            balance -= 1
            current_group += char
            # If the balance is zero, the current group is complete and can be added to the list of separate groups
            if balance == 0:
                separate_groups.append(current_group)
                current_group = ""
    
    # If there are any remaining characters in the current group, it does not have a matching close parenthesis
    if balance!= 0:
        raise ValueError("Unbalanced parentheses: '(' without matching ')'")
    
    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script will solve the problem as described in the provided example. It goes through the string of parentheses once, keeping track of the balance of open and close parentheses. When the balance reaches zero, it means a group of parentheses is complete, and this group is added to the list of separate groups. If the balance does not reach zero, it means there is an unbalanced group, and an error is raised.
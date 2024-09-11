```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
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
        
        # If the balance is zero, it means we've reached the end of a group
        if balance == 0:
            # Add the current group to the list of separated groups
            separated_groups.append(current_group)
            # Reset the current group and balance
            current_group = ""
            balance = 0
    
    # Return the list of separated groups
    return separated_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a simple iterative approach to separate the groups of parentheses. It keeps track of the balance of parentheses by incrementing the counter when it encounters an open parenthesis and decrementing it when it encounters a close parenthesis. When the balance becomes zero, it means we've reached the end of a group, so it adds the current group to the list of separated groups and resets the current group and balance.
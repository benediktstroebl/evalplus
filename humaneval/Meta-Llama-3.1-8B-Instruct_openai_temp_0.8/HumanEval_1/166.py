```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, separates them into balanced groups, 
    and returns a list of these groups.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of balanced groups of parentheses.
    """
    # Remove leading and trailing spaces from the input string
    paren_string = paren_string.strip()
    
    # Initialize an empty list to store the balanced groups
    groups = []
    
    # Initialize an empty string to store the current group being processed
    current_group = ''
    
    # Initialize a counter to track the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance counter
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrement the balance counter
        elif char == ')':
            balance -= 1
            current_group += char
            # If the balance counter reaches zero, it means we have found a balanced group
            if balance == 0:
                groups.append(current_group)
                current_group = ''
    
    # Return the list of balanced groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, separates them into balanced groups, and returns a list of these groups. It iterates over each character in the input string, keeping track of the balance of parentheses and appending the current group to the list of groups when a balanced group is found. The function returns the list of groups. The script then tests the function with the example provided.
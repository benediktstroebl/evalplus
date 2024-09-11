```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate a string of nested parentheses into individual balanced groups.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a balanced group of parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty string to store the current group being processed
    current_group = ''
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a closing parenthesis, decrease the balance
        elif char == ')':
            balance -= 1
            current_group += char
            
            # If the balance is zero, it means we've reached the end of a group
            if balance == 0:
                result.append(current_group)
                current_group = ''
    
    # Return the list of balanced groups
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a counter to keep track of the balance of parentheses. When the balance is zero, it means we've reached the end of a group, so the current group is added to the result list. The function then continues processing the input string until all groups have been separated and added to the result list.
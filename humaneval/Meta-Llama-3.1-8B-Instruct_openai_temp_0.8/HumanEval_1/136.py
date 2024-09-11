```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty string to build the current group
    group = ''
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
            group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            group += char
            # If the balance is zero, it means we have a complete group
            if balance == 0:
                groups.append(group)
                group = ''
        # If the character is not a parenthesis, skip it
    
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of balanced nested parentheses as input and returns a list of strings, each representing a separate group of balanced nested parentheses. The function uses a stack-like approach to keep track of the balance of parentheses and separate the groups. The test case at the end demonstrates the function's behavior.
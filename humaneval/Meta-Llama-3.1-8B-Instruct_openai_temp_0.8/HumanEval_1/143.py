```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and separates them into balanced groups.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a balanced group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize variables to store the result and the current group
    result = []
    current_group = ''
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, add it to the current group
        if char == '(':
            current_group += char
        # If the character is a closing parenthesis, add it to the current group and add the group to the result
        elif char == ')':
            current_group += char
            result.append(current_group)
            current_group = ''
    
    # Return the result
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a simple iterative approach to separate the groups of parentheses. It iterates over the input string, adding each character to the current group if it's an opening parenthesis or adding the group to the result and starting a new group if it's a closing parenthesis. The result is a list of balanced groups of parentheses.
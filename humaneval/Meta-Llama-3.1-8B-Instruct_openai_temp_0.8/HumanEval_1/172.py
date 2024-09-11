```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a group of balanced nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty stack to store the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            stack.pop()
            current_group += char
        
        # If the stack is empty after processing the current character, 
        # it means we have found a complete group, so add it to the result list
        if not stack:
            result.append(current_group)
            current_group = ''
    
    # Return the list of groups
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, where each string represents a group of balanced nested parentheses. The function removes spaces from the input string, iterates over each character, and uses a stack to keep track of the opening parentheses. When a complete group is found, it is added to the result list. Finally, the function returns the list of groups.
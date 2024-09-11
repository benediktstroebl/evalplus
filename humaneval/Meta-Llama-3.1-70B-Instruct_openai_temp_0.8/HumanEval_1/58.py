```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize an empty list to store the groups of parentheses
    groups = []
    
    # Initialize an empty stack to track the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over each character in the input string, ignoring spaces
    for char in paren_string.replace(' ', ''):
        # If the character is an opening parenthesis, add it to the stack and the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, remove the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty after removing the opening parenthesis, it means we've found a complete group
            if not stack:
                groups.append(current_group)
                current_group = ''
    
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
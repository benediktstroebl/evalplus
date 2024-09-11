```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of multiple groups of nested parentheses into a list of strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the groups of parentheses
    groups = []
    
    # Initialize an empty stack to keep track of the parentheses
    stack = []
    
    # Initialize an empty string to build the current group of parentheses
    group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it to the stack and add it to the group
        if char == '(':
            stack.append(char)
            group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add it to the group
        elif char == ')':
            stack.pop()
            group += char
            # If the stack is empty after popping, it means we've found a complete group of parentheses
            if not stack:
                groups.append(group)
                group = ''
    
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
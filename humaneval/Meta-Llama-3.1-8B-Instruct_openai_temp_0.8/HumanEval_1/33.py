```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the groups
    groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over the characters in the string
    for paren in paren_string:
        # If the character is an opening parenthesis, push it to the stack and add it to the current group
        if paren == '(':
            stack.append(paren)
            current_group += paren
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group. If the stack is empty, it means we have found a complete group
        elif paren == ')':
            if stack:
                stack.pop()
                current_group += paren
                # If the stack is empty after popping, it means we have a complete group, so add it to the list of groups
                if not stack:
                    groups.append(current_group)
                    current_group = ''
            # If the stack is empty and we encounter a closing parenthesis, it means the input string is not properly formatted
            else:
                raise ValueError("Invalid input string")
    
    # If there are opening parentheses left in the stack, it means the input string is not properly formatted
    if stack:
        raise ValueError("Invalid input string")
    
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
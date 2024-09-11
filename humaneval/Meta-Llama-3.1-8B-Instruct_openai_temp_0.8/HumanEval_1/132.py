```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of individual string groups of nested parentheses.
    """
    group_stack = []
    groups = []
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            group_stack.append(char)
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            if group_stack:
                group_stack.pop()
            # If the stack is empty after popping, it means we've found a complete group
            if not group_stack:
                # Join the characters in the group and add it to the list of groups
                groups.append("".join(group_stack))
                group_stack = []
    
    # If there are any remaining open parentheses in the stack, it means the input string is not balanced
    if group_stack:
        raise ValueError("Input string is not balanced")
    
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
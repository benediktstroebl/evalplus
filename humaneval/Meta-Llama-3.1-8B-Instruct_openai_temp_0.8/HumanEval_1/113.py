```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into individual strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for paren in paren_string:
        
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if paren == "(":
            stack.append(paren)
            current_group += paren
        
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group
        elif paren == ")":
            stack.pop()
            current_group += paren
            
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                separate_groups.append(current_group)
                current_group = ""
    
    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
print(separate_paren_groups('((()))(())()()(()())'))  # Output: ['((()))', '(())', '()', '()', '(()())']
```

This script uses a stack to keep track of the opening parentheses and a string to build the current group. When a closing parenthesis is encountered and the stack is empty, it means we've found a complete group, so the current group is added to the list of separate groups and the current group is reset.
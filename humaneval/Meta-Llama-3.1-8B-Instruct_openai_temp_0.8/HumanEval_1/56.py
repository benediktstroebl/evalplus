```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses from an input string into a list of strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize an empty stack to keep track of the nested groups
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack and add the close parenthesis to the current group
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group, so add it to the list and reset the current group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means there's a close parenthesis without a corresponding open parenthesis, so raise a ValueError
                raise ValueError("Unbalanced parentheses")
    
    # If there are any remaining open parentheses in the stack, it means there are unbalanced parentheses, so raise a ValueError
    if stack:
        raise ValueError("Unbalanced parentheses")
    
    # Return the list of separate groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate groups of parentheses. The function uses a stack to keep track of the nested groups, and it iterates over each character in the input string to build the current group and add it to the list of groups when it's complete. The function also includes error checking to ensure that the input string has balanced parentheses.
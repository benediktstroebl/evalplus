```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses in a given string into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a separate group of balanced nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            # If the stack is empty and we encounter a closing parenthesis, it means the input string is not balanced
            else:
                raise ValueError("Unbalanced parentheses in the input string")
    
    # If there are any remaining characters in the stack, it means the input string is not balanced
    if stack:
        raise ValueError("Unbalanced parentheses in the input string")
    
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
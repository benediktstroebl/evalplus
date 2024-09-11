```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses and returns a list of those groups.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, where each string is a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the groups of parentheses
    groups = []
    
    # Initialize an empty stack to keep track of the starting index of each group
    stack = []
    
    # Initialize the start index of the current group
    start = 0
    
    # Iterate over the string
    for end, char in enumerate(paren_string):
        # If the character is an opening parenthesis, push the current index onto the stack
        if char == '(':
            stack.append(end)
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty, pop the index from the stack
            if stack:
                stack.pop()
                # If the stack is empty, it means we've found a complete group
                if not stack:
                    # Add the current group to the list of groups
                    groups.append(paren_string[start:end+1])
                    # Reset the start index
                    start = end + 1
    
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string containing multiple groups of nested parentheses and returns a list of those groups. It uses a stack to keep track of the starting index of each group and iterates over the string to find the complete groups. The function also removes spaces from the input string and ignores any errors in the input string.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates balanced groups of parentheses in a given string into individual strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty stack to keep track of opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        else:
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've reached the end of a group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
    
    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. It uses a stack to keep track of opening parentheses and builds the current group by iterating over the characters in the input string. When it encounters a closing parenthesis and the stack is empty, it means we've reached the end of a group, so it adds the current group to the list and resets the current group. The function finally returns the list of separated groups.
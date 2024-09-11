```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced nested parentheses in a string into individual strings.

    Args:
    paren_string (str): The input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of balanced nested parentheses.
    """
    
    stack = []
    groups = []
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add it to the current group
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group, so add it to the list of groups and reset the current group
            if not stack:
                groups.append(current_group)
                current_group = ""
        # If the character is not a parenthesis, just add it to the current group (but only if it's not a space)
        elif char!= " ":
            current_group += char

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script will output:
```
['()', '(())', '(()())']
```
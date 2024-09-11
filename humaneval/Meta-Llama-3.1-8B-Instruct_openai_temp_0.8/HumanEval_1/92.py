### Separate Parenthesis Groups
#### Problem Description
Given a string of multiple groups of nested parentheses, separate the groups into individual strings and return them as a list.

#### Code
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    - paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    - List[str]: List of separate groups of nested parentheses as strings.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add it to the current group
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means there's a mismatched closing parenthesis, so we ignore it
                pass

    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
#### Explanation
This script works by iterating over the input string and keeping track of the opening parentheses using a stack. When a closing parenthesis is encountered, it checks if the stack is empty. If it is, it means we've found a complete group and adds it to the list of groups. If the stack is not empty, it pops the corresponding opening parenthesis and adds the closing parenthesis to the current group. If the stack is empty when a closing parenthesis is encountered, it ignores the mismatched parenthesis.
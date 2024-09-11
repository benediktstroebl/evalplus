### Separate Parentheses Groups

Here's a Python script that uses a stack-based approach to solve this problem.

```markdown
### separate_paren_groups.py
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separated groups of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of open parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # Pop the corresponding open parenthesis from the stack
            stack.pop()
            # Add the close parenthesis to the current group
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group
                current_group = ""

    # Return the list of separated groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated groups. It uses a stack to keep track of open parentheses and iterates over the input string to build the current group. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack and adds the close parenthesis to the current group. If the stack is empty after popping, it means we've found a complete group, so it adds the current group to the list of groups and resets the current group. Finally, it returns the list of separated groups.
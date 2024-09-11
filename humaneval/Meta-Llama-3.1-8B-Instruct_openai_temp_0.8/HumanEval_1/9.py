### Separate Paren Groups

The following Python script solves the problem by using a stack data structure to track the opening and closing parentheses.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string and return them as a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack and list to store the groups
    stack = []
    groups = []

    # Initialize the current group as an empty string
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is empty, it means there's a closing parenthesis without an opening one
            if not stack:
                continue
            # Pop the opening parenthesis from the stack
            stack.pop()
            # Add the closing parenthesis to the current group
            current_group += char

            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script works by iterating over each character in the input string. When it encounters an opening parenthesis, it pushes it onto the stack and adds it to the current group. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack and adds the closing parenthesis to the current group. If the stack is empty after popping, it means we've found a complete group, so it adds the current group to the list of groups and resets the current group. Finally, it returns the list of groups.
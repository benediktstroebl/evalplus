```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string represents a separate group of nested parentheses.
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
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is not empty (i.e., we have a matching opening parenthesis), pop it from the stack
            if stack:
                stack.pop()
                current_group += char
            # If the stack is empty (i.e., we have a closing parenthesis without a matching opening one), ignore it
            else:
                continue
        # If the stack is empty (i.e., we have a character that is not a parenthesis), ignore it

    # If the stack is empty (i.e., all parentheses were matched), add the current group to the list of separate groups
    if not stack:
        separate_groups.append(current_group)

    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

The script uses a stack to keep track of the opening parentheses and a string to build the current group. It iterates over each character in the input string, pushing opening parentheses onto the stack and popping them when it encounters a matching closing parenthesis. When it encounters a closing parenthesis without a matching opening one, it ignores it. When it encounters a character that is not a parenthesis, it ignores it. Finally, it adds the current group to the list of separate groups if all parentheses were matched.
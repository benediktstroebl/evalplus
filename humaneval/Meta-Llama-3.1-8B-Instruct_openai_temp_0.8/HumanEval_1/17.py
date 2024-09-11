```markdown
### Separate Parenthesis Groups
#### Problem Description
Separate groups of nested parentheses in a given string into a list of separate strings.

#### Solution
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a given string into a list of separate strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a stack to keep track of the opening parentheses and the current group
    stack = []
    groups = []

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parenthesis
        elif char == ')':
            # Pop the corresponding opening parenthesis from the stack
            stack.pop()
            # If the stack is empty after popping, it means we've reached the end of a group
            if not stack:
                # Add the current group to the list of groups
                groups.append(paren_string[paren_string.index('(')+1:paren_string.index(')', paren_string.index('('))])

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, removes spaces, and separates the groups into a list of strings. The function uses a stack to keep track of the opening parentheses and identifies the end of each group when it encounters a closing parenthesis that does not have a corresponding opening parenthesis. The function then adds each group to the list and returns it.
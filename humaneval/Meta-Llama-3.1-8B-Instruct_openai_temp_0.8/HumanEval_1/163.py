### Parenthesis Group Separator
#### Problem: Separate nested parentheses groups into individual strings
### Solution

```markdown
### Code
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate nested parentheses groups into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of balanced parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it to the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is empty, it means the current group is not balanced, skip it
            if not stack:
                continue
            # Pop the corresponding opening parenthesis from the stack
            stack.pop()
            # Add the closing parenthesis to the current group
            current_group += char
            # If the stack is empty, it means the current group is balanced, add it to the result
            if not stack:
                result.append(current_group)
                current_group = ''

    # Return the list of separated groups
    return result


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
### Explanation

This script uses a stack to keep track of the opening parentheses and a loop to iterate over the input string. When it encounters an opening parenthesis, it pushes it to the stack and adds it to the current group. When it encounters a closing parenthesis, it checks if the stack is empty, which would indicate an unbalanced group and skips it. If the stack is not empty, it pops the corresponding opening parenthesis from the stack, adds the closing parenthesis to the current group, and checks if the stack is empty. If the stack is empty, it means the current group is balanced, adds it to the result, and resets the current group. This process continues until the entire input string is processed, and the final result is returned.
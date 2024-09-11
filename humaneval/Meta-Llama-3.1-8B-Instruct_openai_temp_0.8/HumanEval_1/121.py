### Separate Paren Groups

Below is a Python script that uses a stack data structure to solve the problem. The script iterates over the input string, pushing opening parentheses onto the stack and popping when a closing parenthesis is encountered, indicating the end of a separate group.

```markdown
### Code
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a stack to keep track of opening parentheses
    stack = []

    # Initialize a list to store separate groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                current_group += char
            # If the stack is empty, it means we've encountered a closing parenthesis
            # without a corresponding opening parenthesis. This is a valid separator
            # between groups, so add the current group to the list and reset it
            else:
                groups.append(current_group)
                current_group = ''

    # Add the last group to the list if it's not empty
    if current_group:
        groups.append(current_group)

    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

### Explanation

*   The script starts by removing spaces from the input string and initializing a stack to keep track of opening parentheses.
*   It then iterates over the input string, pushing opening parentheses onto the stack and popping when a closing parenthesis is encountered.
*   When a closing parenthesis without a corresponding opening parenthesis is encountered, it means we've reached the end of a separate group, so the current group is added to the list and reset.
*   Finally, the script adds the last group to the list if it's not empty and returns the list of separate groups.
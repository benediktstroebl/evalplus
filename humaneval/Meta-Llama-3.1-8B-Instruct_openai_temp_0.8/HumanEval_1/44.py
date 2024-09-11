Here is a Python script that uses a stack to separate the groups of nested parentheses:
```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    paren_string = paren_string.replace(' ', '')  # Remove spaces from the input string
    result = []  # List to store the separate groups
    stack = []  # Stack to keep track of the groups
    current_group = ''  # String to build the current group

    for char in paren_string:
        if char == '(':
            # If we encounter an open parenthesis, start a new group
            if not current_group:  # If we're not building a group yet, start now
                current_group += char
            else:
                stack.append(current_group)  # Otherwise, push the current group onto the stack
                current_group = char  # Reset the current group to the open parenthesis
        elif char == ')':
            # If we encounter a close parenthesis, add it to the current group
            current_group += char

            # If the stack is not empty, pop the previous group and add it to the result
            if stack:
                result.append(stack.pop())
            # Add the current group to the result
            result.append(current_group)
            current_group = ''

    # If there's a group left in the stack after processing all characters, add it to the result
    if stack:
        result.append(stack.pop())
    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script first removes any spaces from the input string. It then iterates over the characters in the string, keeping track of the current group of parentheses. When it encounters a close parenthesis, it adds the current group to the result list and resets the current group. If it encounters an open parenthesis while building a group, it pushes the current group onto the stack and starts a new group. After processing all characters, it checks if there are any groups left in the stack and adds them to the result list.
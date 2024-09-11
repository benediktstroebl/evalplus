```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in the input string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of nested parentheses.

    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack
    stack = []
    # Initialize an empty list to store the groups
    groups = []

    # Initialize an empty string to build the current group
    curr_group = ""

    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack
        if char == "(":
            stack.append(char)
            curr_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # If the stack is not empty, pop the corresponding open parenthesis from the stack
            if stack:
                stack.pop()
                curr_group += char
                # If the stack is now empty, it means we have a complete group, so add it to the list
                if not stack:
                    groups.append(curr_group)
                    curr_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the open parentheses and a list to store the groups. When a close parenthesis is encountered and the stack is not empty, it pops the corresponding open parenthesis from the stack and adds it to the current group. If the stack becomes empty after popping, it means we have a complete group, so we add it to the list. Finally, we return the list of groups.
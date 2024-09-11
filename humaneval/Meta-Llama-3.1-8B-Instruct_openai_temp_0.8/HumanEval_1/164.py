```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, separates it into balanced groups, 
    and returns them as a list of strings. Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    stack = []  # Initialize an empty stack to keep track of parentheses
    groups = []  # Initialize an empty list to store the separate groups
    current_group = ""  # Initialize an empty string to build the current group

    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            else:
                raise ValueError("Unbalanced parentheses: extra closing parenthesis")

    if stack:
        raise ValueError("Unbalanced parentheses: extra opening parenthesis")

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the parentheses in the input string. It iterates through the string, adding characters to the current group as long as the stack is not empty (i.e., we have not yet encountered a closing parenthesis). When a closing parenthesis is encountered and the stack is not empty, it means we have found a complete group, so we add it to the list of groups and reset the current group. If we encounter an extra closing parenthesis, it means the input string is unbalanced. Finally, we return the list of groups.
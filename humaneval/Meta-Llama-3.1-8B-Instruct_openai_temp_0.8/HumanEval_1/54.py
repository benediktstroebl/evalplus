```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, and separates the balanced groups into a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a balanced group of parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the balanced groups
    groups = []

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
            # If the stack is not empty (meaning we have a matching opening parenthesis)
            if stack:
                # Pop the opening parenthesis from the stack
                stack.pop()
                # Add the closing parenthesis to the current group
                current_group += char
                # If the stack is now empty (meaning we have a complete group)
                if not stack:
                    # Add the current group to the list of groups
                    groups.append(current_group)
                    # Reset the current group and the stack
                    current_group = ""
            # If the stack is empty (meaning we have a closing parenthesis without a matching opening one)
            else:
                # Add the closing parenthesis to the current group
                current_group += char

    # Return the list of balanced groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of balanced groups. It uses a stack to keep track of the opening parentheses and builds each group as it iterates over the input string. When a complete group is found, it is added to the list of groups and the current group and stack are reset. The function is then tested with the provided example input.
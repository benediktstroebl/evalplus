```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and returns a list of strings, 
    where each string represents a group of balanced parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, where each string represents a group of balanced parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a stack to keep track of opening parentheses
    stack = []

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is empty, it means there's no matching opening parenthesis, so ignore this closing parenthesis
            if not stack:
                continue
            # Otherwise, pop the opening parenthesis from the stack and add the closing parenthesis to the current group
            else:
                stack.pop()
                current_group += char
                # If the stack is empty, it means we've found a complete group, so add it to the result and reset the current group
                if not stack:
                    result.append(current_group)
                    current_group = ""

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the opening parentheses. When it encounters a closing parenthesis, it checks if the stack is empty. If it is, it means there's no matching opening parenthesis, so it ignores this closing parenthesis. If the stack is not empty, it pops the opening parenthesis from the stack and adds the closing parenthesis to the current group. If the stack becomes empty after popping the opening parenthesis, it means we've found a complete group, so it adds the current group to the result and resets the current group.
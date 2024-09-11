```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings and returns them as a list.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    result.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means there's an unbalanced closing parenthesis, so we ignore it
                pass

    # Return the list of groups
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each representing a separate group of nested parentheses. The function uses a stack to keep track of the opening parentheses and iterates over the input string to build the current group. When a complete group is found, it's added to the result list. Finally, the function returns the list of groups. The script includes a test case to demonstrate the function's behavior.
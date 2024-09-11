```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses, 
    separates them into individual strings and returns the list of those.

    :param paren_string: Input string containing groups of nested parentheses.
    :return: A list of strings, each containing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it to the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty now, it means we've found a complete group
                if not stack:
                    # Add the current group to the result list
                    result.append(current_group)
                    current_group = ""
            # If the stack is empty, it means the closing parenthesis is unmatched
            else:
                # Reset the current group
                current_group = ""

    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string containing groups of nested parentheses, separates them into individual strings, and returns the list of those. It uses a stack to keep track of the opening parentheses and builds the current group by iterating over each character in the input string. The function also handles the case where the closing parenthesis is unmatched by resetting the current group. The script includes a test case to demonstrate the function's correctness.
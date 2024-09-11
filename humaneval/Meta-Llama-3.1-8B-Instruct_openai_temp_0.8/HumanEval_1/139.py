```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into individual strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty stack and a list to store the result
    stack = []
    result = []

    # Initialize an empty string to build each group of parentheses
    group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        # and add the close parenthesis to the current group
        elif char == ')':
            if stack:
                stack.pop()
                group += char
                # If the stack is empty after popping, it means we've found a complete group
                # Add the group to the result list and reset the group
                if not stack:
                    result.append(group)
                    group = ''

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. It uses a stack to keep track of the opening parentheses and a list to store the result. For each group of parentheses, it builds a string by iterating over the input string and popping the corresponding opening parenthesis from the stack when a closing parenthesis is encountered. The script includes a test case at the end to demonstrate the function's usage.
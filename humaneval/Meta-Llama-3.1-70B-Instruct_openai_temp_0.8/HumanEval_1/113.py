```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of parentheses.

    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have found a complete group of parentheses
            if not stack:
                result.append(current_group)
                current_group = ""

    # Return the list of groups of parentheses
    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each representing a group of parentheses. The function uses a stack to keep track of the opening parentheses and builds the current group of parentheses as it iterates over the input string. When it encounters a closing parenthesis that matches an opening parenthesis, it adds the current group to the result list and resets the current group. The function ignores any spaces in the input string and returns the list of groups of parentheses.
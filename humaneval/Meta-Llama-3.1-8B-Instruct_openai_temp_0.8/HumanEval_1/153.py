```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack and a list to store the result
    stack = []
    result = []

    # Initialize a variable to store the current group
    curr_group = ""

    # Iterate over the characters in the string
    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack and add it to the current group
        if char == "(":
            stack.append(char)
            curr_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        # and add the close parenthesis to the current group
        elif char == ")":
            stack.pop()
            curr_group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                result.append(curr_group)
                curr_group = ""

    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each representing a separate group of nested parentheses. The function uses a stack to keep track of the open parentheses and a variable to store the current group. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack and adds the close parenthesis to the current group. If the stack is empty after popping, it means we've found a complete group, which is then added to the result list.
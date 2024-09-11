```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and returns a list of strings where each string
    is a separate group of balanced parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a separate group of balanced parentheses.
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is empty, it means there's a mismatched closing parenthesis, so ignore it
            if not stack:
                continue
            # Otherwise, pop the corresponding opening parenthesis from the stack and add the closing parenthesis to the current group
            else:
                stack.pop()
                current_group += char
        # If the character is not a parenthesis, ignore it
        else:
            continue

        # If the stack is empty after processing the current character, it means we've found a separate group
        if not stack:
            # Add the current group to the list of groups and reset the current group
            groups.append(current_group)
            current_group = ""

    # If the stack is not empty after processing the entire string, it means there are unmatched opening parentheses
    if stack:
        raise ValueError("Unmatched opening parentheses")

    # Return the list of separated groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input, 
    separates those groups into separate strings, and returns a list of those.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    result = []

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
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have a complete group
            if not stack:
                result.append(current_group)
                current_group = ""

    return result


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

In this script, we first remove any spaces from the input string. Then, we initialize an empty list to store the separated groups and an empty stack to keep track of the opening parentheses. We also initialize an empty string to build the current group.

We iterate over each character in the input string. If the character is an opening parenthesis, we push it onto the stack and add it to the current group. If the character is a closing parenthesis, we pop the corresponding opening parenthesis from the stack and add it to the current group. If the stack is empty after popping, it means we have a complete group, so we add it to the result list and reset the current group.

Finally, we return the list of separated groups.
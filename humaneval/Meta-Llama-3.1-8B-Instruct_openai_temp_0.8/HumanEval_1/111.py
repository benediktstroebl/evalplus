```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses and returns a list of strings.
    Each string in the list represents a separate group of balanced parentheses.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of open parentheses
    stack = []

    # Initialize an empty string to build each group
    group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack and add it to the group
        if char == "(":
            stack.append(char)
            group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        # and add it to the group
        elif char == ")":
            if stack:
                stack.pop()
                group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    result.append(group)
                    group = ""
            # If the stack is empty, it means there's a closing parenthesis without a corresponding open one
            else:
                raise ValueError("Invalid input: Unbalanced parentheses")

    # If there are any open parentheses left in the stack, it means the input string is not balanced
    if stack:
        raise ValueError("Invalid input: Unbalanced parentheses")

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each representing a separate group of balanced parentheses. The function uses a stack to keep track of open parentheses and a string to build each group. It iterates over the input string, pushing open parentheses to the stack and adding them to the group. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack and adds it to the group. If the stack is empty after popping, it means we've found a complete group, which is added to the result list. Finally, the function returns the list of separate groups.
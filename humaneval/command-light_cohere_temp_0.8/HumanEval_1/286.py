```python
from typing import List

def separate_paren_groups(parenthes: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of separated parenthesis groups.
    Each group of parentheses should be separated while maintaining balance (each open parent is properly closed).
    Returns: empty list if the input is empty.
    """
    balanced parentheses are not nested and spaces are ignored
    """

    if not parenthes:
        return []

    # Initialize an empty list to store the output
    output = []

    # Iterate through the input string
    for parent in parenthes:
        # Use stack to keep track of open parentheses
        stack = []

        for i, char in enumerate(parent):
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    output.append(parent[:i])
                    stack.pop()
               
                close parentheses
                """ pop from the stack and append the closing parenthesis to the output
                """
                break
        else:
            # Keep the character in the output since it's not a closing parenthesis
                output.append(char)

    return output
```
This Python code defines a function called `separate_paren_groups` that takes a string containing multiple groups of parentheses and returns a list of separated parenthesis groups. The function uses an input string and a stack to keep track of open parentheses. It iterates through through the balanced parentheses and close them, ignoring spaces. The output is then appended to the list of separated groups, which are returned as the function's output.